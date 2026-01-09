# React/Node Assessment Prep

A comprehensive practice project covering all key concepts for a React/Node TypeScript live coding assessment.

## Quick Start

```bash
# Install and run backend
cd backend
npm install
npm run dev

# In another terminal, install and run frontend
cd frontend
npm install
npm run dev
```

- **Frontend**: http://localhost:3000
- **Backend**: http://localhost:3001

---

## 📚 React/Frontend Concepts

### 1. React Hooks

| Hook | Purpose | When to Use |
|------|---------|-------------|
| `useState` | Simple state management | Local component state |
| `useEffect` | Side effects, lifecycle | Data fetching, subscriptions, DOM manipulation |
| `useCallback` | Memoize functions | Pass stable callbacks to optimized children |
| `useMemo` | Memoize values | Expensive calculations, derived data |
| `useRef` | Mutable ref, DOM access | Store values without triggering re-render |
| `useReducer` | Complex state logic | Multiple sub-values, complex transitions |

### 2. Re-renders and Hook Behavior

```tsx
// Component re-renders when:
// 1. State changes (useState, useReducer)
// 2. Props change
// 3. Parent re-renders
// 4. Context value changes

// Hook execution during render:
function Component() {
  // Hooks called in same order every render
  const [count, setCount] = useState(0);  // Runs every render
  
  useEffect(() => {
    // Runs AFTER render commits to DOM
    return () => {
      // Cleanup runs before next effect and on unmount
    };
  }, [count]); // Only when count changes
}
```

### 3. Derived State vs Stored State

```tsx
// ❌ BAD: Storing derived state
const [items, setItems] = useState([]);
const [itemCount, setItemCount] = useState(0);
useEffect(() => setItemCount(items.length), [items]);

// ✅ GOOD: Derive the value
const [items, setItems] = useState([]);
const itemCount = items.length; // Computed on render
```

### 4. Performance Optimization

```tsx
// React.memo - Skip re-render when props unchanged
const Child = memo(({ value }) => <div>{value}</div>);

// useCallback - Stable function reference
const handleClick = useCallback(() => {
  doSomething();
}, []); // Empty deps = never recreates

// useMemo - Expensive calculation
const sortedItems = useMemo(() => {
  return items.sort((a, b) => a.name.localeCompare(b.name));
}, [items]); // Only when items changes
```

### 5. Effect Lifecycle

```tsx
useEffect(() => {
  // SETUP: Runs after render
  const subscription = subscribe(id);
  
  return () => {
    // CLEANUP: Runs before next effect or unmount
    subscription.unsubscribe();
  };
}, [id]); // DEPENDENCIES: Run when these change

// Common patterns:
// [] = run once on mount, cleanup on unmount
// [dep] = run when dep changes
// no array = run every render (AVOID!)
```

### 6. Debounce vs Throttle

| Technique | Behavior | Use Case |
|-----------|----------|----------|
| **Debounce** | Wait until activity stops | Search input, form validation |
| **Throttle** | Limit to once per interval | Scroll, resize, mousemove |

```tsx
// Debounced value hook
function useDebouncedValue<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState(value);
  
  useEffect(() => {
    const timeout = setTimeout(() => setDebouncedValue(value), delay);
    return () => clearTimeout(timeout);
  }, [value, delay]);
  
  return debouncedValue;
}
```

### 7. Data Fetching with Fetch API

```tsx
const fetchData = async () => {
  setLoading(true);
  try {
    const response = await fetch('/api/data');
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data: MyType = await response.json();
    setData(data);
  } catch (error) {
    const message = error instanceof Error ? error.message : 'Unknown error';
    setError(message);
  } finally {
    setLoading(false);
  }
};
```

---

## 🖥️ Backend/Node Concepts

### 1. Error Handling in Different Execution Paths

```typescript
// SYNCHRONOUS - Caught by Express automatically
app.get('/sync', (req, res) => {
  throw new Error('Sync error'); // Express catches this
});

// ASYNC/AWAIT - Need try-catch or wrapper
app.get('/async', async (req, res, next) => {
  try {
    await riskyOperation();
  } catch (error) {
    next(error); // Pass to error handler
  }
});

// PROMISE - Must handle rejection
app.get('/promise', (req, res, next) => {
  doSomething()
    .then(result => res.json(result))
    .catch(next); // Always handle!
});

// CALLBACK - Error-first pattern
fs.readFile('file.txt', (err, data) => {
  if (err) return next(err);
  res.send(data);
});

// PROCESS-LEVEL
process.on('uncaughtException', (error) => { /* log and exit */ });
process.on('unhandledRejection', (reason) => { /* log */ });
```

### 2. Handling Spiky Traffic

| Strategy | Description |
|----------|-------------|
| **Rate Limiting** | Limit requests per time window per client |
| **Queuing** | Buffer requests, process at sustainable rate |
| **Circuit Breaker** | Fail fast when downstream services down |
| **Caching** | Reduce backend load with cached responses |
| **Load Balancing** | Distribute across multiple servers |

### 3. Scaling Services

| Approach | Pros | Cons |
|----------|------|------|
| **Vertical (Scale Up)** | Simple, no code changes | Limited ceiling, single point of failure |
| **Horizontal (Scale Out)** | Unlimited scaling | Requires stateless design, complexity |
| **Auto-scaling** | Automatic, cost-efficient | Cold start latency, configuration |
| **Serverless** | Zero idle cost, auto-scales | Cold starts, vendor lock-in |

### 4. Authentication Models

| Model | How it Works | Best For |
|-------|--------------|----------|
| **Session** | Server stores session, client gets cookie | Traditional web apps |
| **JWT** | Signed token with claims, client stores | SPAs, microservices |
| **OAuth 2.0** | Delegated auth with third party | Social login, API access |
| **API Keys** | Static key in header | Service-to-service |

```typescript
// JWT Authentication
const token = jwt.sign({ id: user.id }, SECRET, { expiresIn: '1h' });

// Verify middleware
const authenticate = (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  const decoded = jwt.verify(token, SECRET);
  req.user = decoded;
  next();
};
```

### 5. Caching Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Cache-aside** | Check cache, fetch if miss, update cache | Read-heavy workloads |
| **Write-through** | Write to cache and DB simultaneously | Consistency required |
| **Write-behind** | Write to cache, async write to DB | High write throughput |

### 6. API Design Styles

| Style | Characteristics | Best For |
|-------|-----------------|----------|
| **REST** | Resource-based URLs, HTTP methods | Standard CRUD APIs |
| **GraphQL** | Single endpoint, client specifies fields | Complex data needs |
| **gRPC** | Binary protocol, strongly typed | Microservices |
| **WebSocket** | Full-duplex, persistent connection | Real-time apps |

### 7. Rendering Models

| Model | When HTML Generated | Trade-offs |
|-------|---------------------|------------|
| **CSR** | Client (JavaScript) | Fast transitions, slow initial, SEO issues |
| **SSR** | Server (per request) | Good SEO, higher server load |
| **SSG** | Build time | Fastest, only for static content |
| **ISR** | Build + on-demand | Balance of SSG and SSR |

---

## 🎯 Live Coding Tips

1. **Think aloud** - Explain your thought process
2. **Start simple** - Get working code first, optimize later
3. **Handle edge cases** - Empty states, errors, loading
4. **Use TypeScript** - Define types explicitly
5. **Clean up effects** - Always return cleanup functions
6. **Test incrementally** - Verify each step works

---

## 📁 Project Structure

```
react-node-prep/
├── backend/
│   ├── src/
│   │   ├── index.ts          # Entry point, error handling examples
│   │   ├── middleware/
│   │   │   ├── auth.ts       # JWT authentication
│   │   │   ├── errorHandler.ts
│   │   │   └── rateLimiter.ts
│   │   └── routes/
│   │       ├── auth.ts       # Login endpoint
│   │       ├── todos.ts      # CRUD with caching
│   │       └── users.ts      # Pagination example
│   ├── package.json
│   └── tsconfig.json
│
├── frontend/
│   ├── src/
│   │   ├── App.tsx           # Main app with tabs
│   │   ├── components/
│   │   │   ├── HooksDemo.tsx         # useState, useReducer, useRef
│   │   │   ├── PerformanceDemo.tsx   # memo, useCallback, useMemo
│   │   │   ├── DataFetchingDemo.tsx  # Fetch API with types
│   │   │   ├── DebounceThrottleDemo.tsx
│   │   │   └── EffectLifecycleDemo.tsx
│   │   ├── types.ts          # TypeScript interfaces
│   │   └── main.tsx
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   └── tailwind.config.js
│
└── README.md
```

Good luck with your assessment! 🚀
