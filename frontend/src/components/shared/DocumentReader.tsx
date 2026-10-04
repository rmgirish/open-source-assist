import { useEffect, useState } from 'react'
import { BookOpen, ExternalLink, Loader2, RotateCcw } from 'lucide-react'
import { Badge, Button, Dialog } from '@/components/ui'
import { MarkdownView } from '@/components/shared/MarkdownView'
import {
  fetchDocumentDetail,
  recordDocumentView,
  type DocumentDetail,
} from '@/lib/docs-api'
import { useAuthStore } from '@/lib/auth-store'
import { cn } from '@/lib/utils'

interface DocumentReaderProps {
  /** Document id to open; null closes the reader. */
  docId: string | null
  onClose: () => void
}

export function DocumentReader({ docId, onClose }: DocumentReaderProps) {
  const token = useAuthStore((s) => s.token)
  const [detail, setDetail] = useState<DocumentDetail | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    if (!docId) {
      setDetail(null)
      setError(null)
      return
    }
    let cancelled = false
    setLoading(true)
    setError(null)
    setDetail(null)

    fetchDocumentDetail(docId)
      .then((data) => {
        if (cancelled) return
        setDetail(data)
        // Fire-and-forget: feeds personalized recommendations.
        void recordDocumentView(docId, token ?? undefined)
      })
      .catch((err: unknown) => {
        if (!cancelled) {
          setError(err instanceof Error ? err.message : 'Failed to load document')
        }
      })
      .finally(() => {
        if (!cancelled) setLoading(false)
      })

    return () => {
      cancelled = true
    }
  }, [docId, token])

  return (
    <Dialog
      open={docId !== null}
      onClose={onClose}
      ariaLabel="Document reader"
      title={detail ? `$ osa docs read --id ${detail.id}` : '$ osa docs read'}
      className="max-w-[760px]"
    >
      {loading ? (
        <div className="flex min-h-56 items-center justify-center gap-2.5 text-sm text-muted-foreground">
          <Loader2 className="size-4 animate-spin" aria-hidden="true" />
          Loading document…
        </div>
      ) : error ? (
        <div className="flex min-h-56 flex-col items-center justify-center gap-3 px-6 text-center">
          <p className="text-sm text-destructive">{error}</p>
          <Button
            size="sm"
            variant="secondary"
            onClick={() => docId && window.location.reload()}
            className="gap-1.5"
          >
            <RotateCcw className="size-3.5" aria-hidden="true" />
            Retry
          </Button>
        </div>
      ) : detail ? (
        <>
          {/* Header */}
          <div className="shrink-0 border-b border-border px-6 py-5">
            <div className="flex items-start justify-between gap-4">
              <div className="min-w-0">
                <h2 className="text-base font-bold tracking-tight text-foreground">
                  {detail.title}
                </h2>
                <p className="mt-1 font-mono text-[10px] uppercase tracking-wider text-muted-foreground">
                  {detail.source} · {detail.category}
                  {detail.target_skill_level !== 'all' && ` · ${detail.target_skill_level}`}
                </p>
              </div>
              <a
                href={detail.url}
                target="_blank"
                rel="noopener noreferrer"
                className="flex shrink-0 items-center gap-1.5 rounded-md border border-border bg-surface px-2.5 py-1.5 text-[11px] font-medium text-muted-foreground transition-colors hover:border-accent/50 hover:text-foreground"
                title="Open the official source in a new tab"
              >
                <ExternalLink className="size-3" aria-hidden="true" />
                Official source
              </a>
            </div>
            <div className="mt-3 flex flex-wrap items-center gap-1.5">
              {detail.tags.slice(0, 5).map((tag) => (
                <Badge key={tag} variant="outline" className="text-[10px]">
                  {tag}
                </Badge>
              ))}
            </div>
          </div>

          {/* Full document content */}
          <div className="min-h-0 flex-1 overflow-y-auto px-6 py-5">
            <div className="mx-auto max-w-prose">
              <MarkdownView content={detail.content} />
            </div>
          </div>

          {/* Footer */}
          <div
            className={cn(
              'flex shrink-0 items-center justify-between border-t border-border px-6 py-3',
            )}
          >
            <span className="flex items-center gap-1.5 text-[11px] text-muted-foreground">
              <BookOpen className="size-3.5" aria-hidden="true" />
              Read in-app · full document
            </span>
            <Button size="sm" variant="secondary" onClick={onClose}>
              Done
            </Button>
          </div>
        </>
      ) : null}
    </Dialog>
  )
}

export default DocumentReader
