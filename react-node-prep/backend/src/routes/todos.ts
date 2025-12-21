import { Router, Request, Response } from 'express';
import { AppError, asyncHandler } from '../middleware/errorHandler';

export const todosRouter = Router();

// ============================================================
// IN-MEMORY CACHE EXAMPLE
// ============================================================

interface Todo {
  id: string;
  title: string;
  completed: boolean;
  userId: string;
}

// Mock database
let todos: Todo[] = [
  { id: '1', title: 'Learn React hooks', completed: false, userId: '1' },
  { id: '2', title: 'Practice TypeScript', completed: true, userId: '1' },
  { id: '3', title: 'Build a full-stack app', completed: false, userId: '1' },
];

// Simple cache implementation
interface CacheEntry<T> {
  data: T;
  expiry: number;
}

class SimpleCache {
  private cache: Map<string, CacheEntry<unknown>> = new Map();
  private defaultTTL = 60 * 1000; // 1 minute

  get<T>(key: string): T | null {
    const entry = this.cache.get(key);
    if (!entry) return null;
    
    if (Date.now() > entry.expiry) {
      this.cache.delete(key);
      return null;
    }
    
    return entry.data as T;
  }

  set<T>(key: string, data: T, ttl = this.defaultTTL): void {
    this.cache.set(key, {
      data,
      expiry: Date.now() + ttl,
    });
  }

  invalidate(pattern: string): void {
    for (const key of this.cache.keys()) {
      if (key.startsWith(pattern)) {
        this.cache.delete(key);
      }
    }
  }
}

const cache = new SimpleCache();

// ============================================================
// REST API ENDPOINTS
// ============================================================

// GET /api/todos - List all todos (with caching)
todosRouter.get('/', asyncHandler(async (req: Request, res: Response) => {
  // Check cache first
  const cacheKey = 'todos:all';
  const cachedTodos = cache.get<Todo[]>(cacheKey);
  
  if (cachedTodos) {
    res.setHeader('X-Cache', 'HIT');
    res.json(cachedTodos);
    return;
  }

  // Simulate database delay
  await new Promise(resolve => setTimeout(resolve, 100));
  
  // Store in cache
  cache.set(cacheKey, todos);
  res.setHeader('X-Cache', 'MISS');
  res.json(todos);
}));

// GET /api/todos/:id - Get single todo
todosRouter.get('/:id', (req: Request<{ id: string }>, res: Response) => {
  const todo = todos.find(t => t.id === req.params.id);
  
  if (!todo) {
    throw new AppError('Todo not found', 404);
  }
  
  res.json(todo);
});

// POST /api/todos - Create todo
todosRouter.post('/', (req: Request, res: Response) => {
  const { title } = req.body;
  
  if (!title) {
    throw new AppError('Title is required', 400);
  }

  const newTodo: Todo = {
    id: String(Date.now()),
    title,
    completed: false,
    userId: '1',
  };
  
  todos.push(newTodo);
  
  // Invalidate cache
  cache.invalidate('todos');
  
  res.status(201).json(newTodo);
});

// PATCH /api/todos/:id - Update todo
todosRouter.patch('/:id', (req: Request<{ id: string }>, res: Response) => {
  const index = todos.findIndex(t => t.id === req.params.id);
  
  if (index === -1) {
    throw new AppError('Todo not found', 404);
  }
  
  todos[index] = { ...todos[index], ...req.body };
  cache.invalidate('todos');
  
  res.json(todos[index]);
});

// DELETE /api/todos/:id - Delete todo
todosRouter.delete('/:id', (req: Request<{ id: string }>, res: Response) => {
  const index = todos.findIndex(t => t.id === req.params.id);
  
  if (index === -1) {
    throw new AppError('Todo not found', 404);
  }
  
  const deleted = todos.splice(index, 1);
  cache.invalidate('todos');
  
  res.json(deleted[0]);
});

// ============================================================
// CACHING PATTERNS (Verbal Discussion Notes)
// ============================================================

/*
COMMON CACHING PATTERNS:

1. CACHE-ASIDE (Lazy Loading):
   - Check cache first
   - If miss, fetch from DB and populate cache
   - Application manages cache
   - Pros: Only requested data is cached
   - Cons: Cache miss penalty, potential stale data

2. WRITE-THROUGH:
   - Write to cache and DB simultaneously
   - Ensures cache is always up-to-date
   - Pros: Consistent data
   - Cons: Write latency, writes to cache may never be read

3. WRITE-BEHIND (Write-Back):
   - Write to cache first, async write to DB
   - Pros: Fast writes
   - Cons: Risk of data loss, complexity

4. REFRESH-AHEAD:
   - Proactively refresh frequently accessed items before expiry
   - Pros: Low latency for popular items
   - Cons: Complexity, may refresh unused items

CACHE INVALIDATION STRATEGIES:
- TTL (Time-To-Live): Auto-expire after duration
- Event-based: Invalidate on data changes
- Version-based: Use version number in cache key

CACHE LEVELS:
1. Browser cache (HTTP caching headers)
2. CDN/Edge cache
3. Application-level cache (Redis, Memcached)
4. Database query cache
*/
