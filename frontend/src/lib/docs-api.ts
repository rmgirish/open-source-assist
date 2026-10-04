/**
 * API client for the Official Documentation Hub and personalized docs recommendations.
 */

export interface DocCategory {
  id: string
  label: string
  description: string
}

export interface DocumentItem {
  id: string
  title: string
  description: string
  url: string
  category: string
  source: string
  tags: string[]
  target_skill_level: 'beginner' | 'intermediate' | 'advanced' | 'all'
  is_recommended: boolean
  recommendation_reason?: string | null
  has_full_text?: boolean
}

export interface DocumentDetail extends DocumentItem {
  content: string
}

export interface RecommendationItem {
  document: DocumentItem
  reason: string
  score: number
}

export interface RecommendationsResponse {
  items: RecommendationItem[]
  user_skill_level?: string | null
  user_context?: string | null
  basis: 'reading_history' | 'skill_level' | 'default' | 'none'
}

export interface DocsCatalogResponse {
  categories: DocCategory[]
  items: DocumentItem[]
  total_count: number
  user_skill_level?: string | null
  user_context?: string | null
  is_personalized: boolean
}

export interface FetchDocsParams {
  category?: string
  query?: string
}

/**
 * Fetch official documentation from FastAPI with personalized skill level ranking.
 */
export async function fetchDocuments(
  params?: FetchDocsParams,
  token?: string,
): Promise<DocsCatalogResponse> {
  const queryParams = new URLSearchParams()
  if (params?.category && params.category !== 'all') {
    queryParams.set('category', params.category)
  }
  if (params?.query && params.query.trim()) {
    queryParams.set('query', params.query.trim())
  }

  const qs = queryParams.toString()
  const url = `/api/v1/docs${qs ? `?${qs}` : ''}`

  const headers: Record<string, string> = {
    'Content-Type': 'application/json',
  }
  if (token) {
    headers['Authorization'] = `Bearer ${token}`
  }

  const response = await fetch(url, {
    method: 'GET',
    headers,
  })

  if (!response.ok) {
    throw new Error(await extractApiError(response, 'Failed to fetch documentation'))
  }

  return response.json() as Promise<DocsCatalogResponse>
}

/**
 * Fetch one full document (complete markdown content) for in-app reading.
 */
export async function fetchDocumentDetail(
  docId: string,
): Promise<DocumentDetail> {
  const response = await fetch(`/api/v1/docs/${encodeURIComponent(docId)}`, {
    method: 'GET',
    headers: { 'Content-Type': 'application/json' },
  })

  if (!response.ok) {
    throw new Error(await extractApiError(response, 'Failed to load document'))
  }

  return response.json() as Promise<DocumentDetail>
}

/**
 * Fetch personalized recommendations (reading history + skill level aware).
 */
export async function fetchRecommendations(
  limit = 6,
  token?: string,
): Promise<RecommendationsResponse> {
  const response = await fetch(`/api/v1/docs/recommendations?limit=${limit}`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
  })

  if (!response.ok) {
    throw new Error(await extractApiError(response, 'Failed to fetch recommendations'))
  }

  return response.json() as Promise<RecommendationsResponse>
}

/**
 * Record that the signed-in user opened a document (fire-and-forget).
 */
export async function recordDocumentView(docId: string, token?: string): Promise<void> {
  try {
    await fetch(`/api/v1/docs/${encodeURIComponent(docId)}/view`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        ...(token ? { Authorization: `Bearer ${token}` } : {}),
      },
    })
  } catch {
    // View tracking is best-effort; never block reading.
  }
}

async function extractApiError(response: Response, fallback: string): Promise<string> {
  const errorBody = await response.json().catch(() => null)
  return typeof errorBody?.detail === 'string'
    ? errorBody.detail
    : `${fallback} (${response.status})`
}
