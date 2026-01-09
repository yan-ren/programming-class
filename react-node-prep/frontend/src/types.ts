// ============================================================
// TYPESCRIPT TYPES - Explicit types for UI logic
// ============================================================

export interface Todo {
  id: string;
  title: string;
  completed: boolean;
  userId: string;
}

export interface User {
  id: string;
  name: string;
  email: string;
  role: string;
}

export interface PaginatedResponse<T> {
  data: T[];
  pagination: {
    page: number;
    limit: number;
    total: number;
    totalPages: number;
  };
}

export interface ApiError {
  error: {
    message: string;
    stack?: string;
  };
}

// Generic fetch result type for type-safe data fetching
export type FetchResult<T> =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; data: T }
  | { status: 'error'; error: string };

// Form state type
export interface FormState<T> {
  values: T;
  errors: Partial<Record<keyof T, string>>;
  touched: Partial<Record<keyof T, boolean>>;
  isSubmitting: boolean;
}
