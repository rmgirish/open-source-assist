import * as React from 'react'
import { cn } from '@/lib/utils'

/**
 * Minimal, dependency-free markdown renderer for in-app document reading.
 * Supports: h2/h3, paragraphs, bullet/numbered lists, blockquotes,
 * fenced code blocks (with simple diff highlighting), tables, links,
 * bold/italic/inline-code, and GitHub-style alerts.
 */

type Block =
  | { kind: 'heading'; level: 2 | 3 | 4; text: string }
  | { kind: 'paragraph'; text: string }
  | { kind: 'list'; ordered: boolean; items: string[] }
  | { kind: 'blockquote'; lines: string[] }
  | { kind: 'code'; lang: string; lines: string[] }
  | { kind: 'table'; header: string[]; rows: string[][] }

function parseInline(text: string): React.ReactNode[] {
  const nodes: React.ReactNode[] = []
  // Order matters: links, then code, then bold, then italic.
  const pattern =
    /\[([^\]]+)\]\(([^)\s]+)\)|`([^`]+)`|\*\*([^*]+)\*\*|\*([^*\n]+)\*/g
  let last = 0
  let m: RegExpExecArray | null
  let key = 0

  while ((m = pattern.exec(text)) !== null) {
    if (m.index > last) nodes.push(text.slice(last, m.index))
    if (m[1] !== undefined) {
      nodes.push(
        <a
          key={key++}
          href={m[2]}
          target="_blank"
          rel="noopener noreferrer"
          className="text-accent-text underline decoration-accent/40 underline-offset-2 hover:decoration-accent"
        >
          {m[1]}
        </a>,
      )
    } else if (m[3] !== undefined) {
      nodes.push(
        <code
          key={key++}
          className="rounded bg-surface px-1.5 py-0.5 font-mono text-[0.85em] text-accent-text"
        >
          {m[3]}
        </code>,
      )
    } else if (m[4] !== undefined) {
      nodes.push(
        <strong key={key++} className="font-semibold text-foreground">
          {m[4]}
        </strong>,
      )
    } else if (m[5] !== undefined) {
      nodes.push(
        <em key={key++} className="italic">
          {m[5]}
        </em>,
      )
    }
    last = m.index + m[0].length
  }
  if (last < text.length) nodes.push(text.slice(last))
  return nodes
}

function renderAlert(lines: string[]): React.ReactNode | null {
  const first = lines[0] ?? ''
  const alertMatch = first.match(/^>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*(.*)$/i)
  if (!alertMatch) return null
  const kind = alertMatch[1].toUpperCase()
  const body = [alertMatch[2], ...lines.slice(1).map((l) => l.replace(/^>\s?/, ''))]
    .filter(Boolean)
    .join(' ')

  const styles: Record<string, string> = {
    NOTE: 'border-sky-500/40 bg-sky-500/5',
    TIP: 'border-emerald-500/40 bg-emerald-500/5',
    IMPORTANT: 'border-violet-500/40 bg-violet-500/5',
    WARNING: 'border-amber-500/40 bg-amber-500/5',
    CAUTION: 'border-red-500/40 bg-red-500/5',
  }
  return (
    <div
      key={`alert-${kind}-${body.slice(0, 16)}`}
      className={cn('rounded-lg border-l-4 px-4 py-3 text-xs leading-relaxed', styles[kind])}
    >
      <span className="mb-0.5 block font-mono text-[10px] font-bold uppercase tracking-wider text-foreground">
        {kind}
      </span>
      {parseInline(body)}
    </div>
  )
}

function parseBlocks(markdown: string): Block[] {
  const lines = markdown.split(/\r?\n/)
  const blocks: Block[] = []
  let i = 0

  while (i < lines.length) {
    const line = lines[i]

    if (!line.trim()) {
      i++
      continue
    }

    // Fenced code block
    if (line.trimStart().startsWith('```')) {
      const lang = line.trim().slice(3).trim()
      const body: string[] = []
      i++
      while (i < lines.length && !lines[i].trimStart().startsWith('```')) {
        body.push(lines[i])
        i++
      }
      i++ // closing fence
      blocks.push({ kind: 'code', lang, lines: body })
      continue
    }

    // Heading
    const heading = line.match(/^(#{2,4})\s+(.*)$/)
    if (heading) {
      blocks.push({
        kind: 'heading',
        level: heading[1].length as 2 | 3 | 4,
        text: heading[2],
      })
      i++
      continue
    }

    // Table
    if (line.trim().startsWith('|') && lines[i + 1]?.match(/^\s*\|[\s:|-]+\|\s*$/)) {
      const parseRow = (row: string): string[] =>
        row
          .trim()
          .replace(/^\|/, '')
          .replace(/\|$/, '')
          .split('|')
          .map((c) => c.trim())
      const header = parseRow(line)
      i += 2
      const rows: string[][] = []
      while (i < lines.length && lines[i].trim().startsWith('|')) {
        rows.push(parseRow(lines[i]))
        i++
      }
      blocks.push({ kind: 'table', header, rows })
      continue
    }

    // Blockquote (incl. GitHub alerts)
    if (line.trimStart().startsWith('>')) {
      const quoteLines: string[] = []
      while (i < lines.length && lines[i].trimStart().startsWith('>')) {
        quoteLines.push(lines[i].trimStart())
        i++
      }
      const isAlert = /^>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]/i.test(quoteLines[0] ?? '')
      if (isAlert) {
        blocks.push({ kind: 'paragraph', text: `__ALERT__${quoteLines.join('\n')}` })
      } else {
        blocks.push({
          kind: 'blockquote',
          lines: quoteLines.map((l) => l.replace(/^>\s?/, '')),
        })
      }
      continue
    }

    // Lists
    const bullet = line.match(/^\s*[-*]\s+(.*)$/)
    const numbered = line.match(/^\s*\d+[.)]\s+(.*)$/)
    if (bullet || numbered) {
      const ordered = Boolean(numbered)
      const items: string[] = []
      while (i < lines.length) {
        const b = lines[i].match(/^\s*[-*]\s+(.*)$/)
        const n = lines[i].match(/^\s*\d+[.)]\s+(.*)$/)
        const isSubItem = /^\s{2,}[-*]\s+/.test(lines[i])
        if (isSubItem) {
          // Flatten sub-items into the previous item for simplicity.
          if (items.length > 0) items[items.length - 1] += ` — ${(b ?? n)?.[1]}`
        } else if ((ordered && n) || (!ordered && b)) {
          items.push((b ?? n)![1])
        } else {
          break
        }
        i++
      }
      blocks.push({ kind: 'list', ordered, items })
      continue
    }

    // Paragraph: gather until blank line or another block starter.
    const para: string[] = []
    while (
      i < lines.length &&
      lines[i].trim() &&
      !lines[i].trimStart().startsWith('```') &&
      !lines[i].trimStart().startsWith('>') &&
      !lines[i].trim().startsWith('|') &&
      !/^\s*([-*]|\d+[.)])\s+/.test(lines[i]) &&
      !/^#{2,4}\s/.test(lines[i])
    ) {
      para.push(lines[i])
      i++
    }
    if (para.length) blocks.push({ kind: 'paragraph', text: para.join(' ') })
    else i++ // safety: never loop forever
  }

  return blocks
}

function renderBlock(block: Block, index: number): React.ReactNode {
  const key = `b${index}`
  switch (block.kind) {
    case 'heading': {
      const cls =
        block.level === 2
          ? 'mt-6 border-b border-border pb-1.5 text-base font-bold tracking-tight text-foreground'
          : block.level === 3
            ? 'mt-5 text-sm font-semibold text-foreground'
            : 'mt-4 text-xs font-semibold uppercase tracking-wider text-muted-foreground'
      const Tag = (['h2', 'h3', 'h4'][block.level - 2] ?? 'h4') as 'h2' | 'h3' | 'h4'
      return (
        <Tag key={key} className={cls}>
          {parseInline(block.text)}
        </Tag>
      )
    }
    case 'paragraph': {
      if (block.text.startsWith('__ALERT__')) {
        const alertNode = renderAlert(block.text.slice(9).split('\n').map((l) => `> ${l}`))
        return alertNode
      }
      return (
        <p key={key} className="text-xs leading-relaxed text-muted-foreground">
          {parseInline(block.text)}
        </p>
      )
    }
    case 'list':
      return block.ordered ? (
        <ol key={key} className="ml-4 list-decimal space-y-1.5 text-xs text-muted-foreground">
          {block.items.map((item, j) => (
            <li key={`${key}-${j}`} className="leading-relaxed pl-1">
              {parseInline(item)}
            </li>
          ))}
        </ol>
      ) : (
        <ul key={key} className="ml-4 list-disc space-y-1.5 text-xs text-muted-foreground">
          {block.items.map((item, j) => (
            <li key={`${key}-${j}`} className="leading-relaxed pl-1">
              {parseInline(item)}
            </li>
          ))}
        </ul>
      )
    case 'blockquote':
      return (
        <blockquote
          key={key}
          className="border-l-2 border-accent/50 bg-accent/5 px-4 py-2.5 text-xs italic leading-relaxed text-foreground"
        >
          {parseInline(block.lines.join(' '))}
        </blockquote>
      )
    case 'code': {
      return (
        <pre
          key={key}
          className="overflow-x-auto rounded-lg border border-border bg-surface p-3 font-mono text-[11px] leading-relaxed text-foreground"
        >
          <code>
            {block.lines.map((line, j) => {
              let cls = ''
              if (block.lang === 'diff') {
                if (line.startsWith('+')) cls = 'text-emerald-500'
                else if (line.startsWith('-')) cls = 'text-red-500'
              }
              return (
                <span key={`${key}-${j}`} className={cn('block', cls)}>
                  {line || ' '}
                </span>
              )
            })}
          </code>
        </pre>
      )
    }
    case 'table':
      return (
        <div
          key={key}
          className="overflow-x-auto rounded-lg border border-border"
        >
          <table className="w-full border-collapse text-xs">
            <thead>
              <tr className="border-b border-border bg-surface">
                {block.header.map((cell, j) => (
                  <th
                    key={`${key}-h${j}`}
                    className="px-3 py-2 text-left font-semibold text-foreground"
                  >
                    {parseInline(cell)}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {block.rows.map((row, r) => (
                <tr key={`${key}-r${r}`} className="border-b border-border/50 last:border-0">
                  {row.map((cell, c) => (
                    <td key={`${key}-r${r}c${c}`} className="px-3 py-2 text-muted-foreground">
                      {parseInline(cell)}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )
    default:
      return null
  }
}

export function MarkdownView({ content, className }: { content: string; className?: string }) {
  const blocks = React.useMemo(() => parseBlocks(content), [content])
  return <div className={cn('space-y-3.5', className)}>{blocks.map(renderBlock)}</div>
}

export default MarkdownView
