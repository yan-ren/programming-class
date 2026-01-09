import { Router, Request, Response } from 'express';
import { AppError } from '../middleware/errorHandler';

export const usersRouter = Router();

// Mock user database
const users = [
  { id: '1', name: 'John Doe', email: 'john@example.com', role: 'admin' },
  { id: '2', name: 'Jane Smith', email: 'jane@example.com', role: 'user' },
  { id: '3', name: 'Bob Wilson', email: 'bob@example.com', role: 'user' },
];

// ============================================================
// REST API EXAMPLES
// ============================================================

// GET /api/users - List all users
usersRouter.get('/', (req: Request, res: Response) => {
  // Pagination example
  const page = parseInt(req.query.page as string) || 1;
  const limit = parseInt(req.query.limit as string) || 10;
  const startIndex = (page - 1) * limit;
  const endIndex = page * limit;

  const paginatedUsers = users.slice(startIndex, endIndex);

  res.json({
    data: paginatedUsers,
    pagination: {
      page,
      limit,
      total: users.length,
      totalPages: Math.ceil(users.length / limit),
    },
  });
});

// GET /api/users/:id - Get user by ID
usersRouter.get('/:id', (req: Request<{ id: string }>, res: Response) => {
  const user = users.find(u => u.id === req.params.id);
  
  if (!user) {
    throw new AppError('User not found', 404);
  }
  
  res.json(user);
});

// ============================================================
// API DESIGN STYLES (Verbal Discussion Notes)
// ============================================================

/*
1. REST (Representational State Transfer):
   - Resource-based URLs (/users, /users/123)
   - HTTP methods (GET, POST, PUT, PATCH, DELETE)
   - Stateless
   - Standardized but can lead to over/under-fetching
   
2. GraphQL:
   - Single endpoint (/graphql)
   - Client specifies exactly what data needed
   - Strong typing with schema
   - Reduces over-fetching
   - More complex caching
   
3. gRPC:
   - Binary protocol (Protocol Buffers)
   - High performance, strongly typed
   - Good for microservices
   - Browser support requires grpc-web
   
4. WebSockets:
   - Full-duplex communication
   - Real-time updates
   - Persistent connection

5. Server-Sent Events (SSE):
   - Server pushes to client
   - Simpler than WebSockets
   - One-way communication

RENDERING MODELS:

1. Client-Side Rendering (CSR):
   - JavaScript renders in browser
   - Fast transitions, slower initial load
   - SEO challenges
   - Example: Create React App

2. Server-Side Rendering (SSR):
   - HTML generated on server per request
   - Good for SEO, faster first paint
   - Higher server load
   - Example: Next.js with getServerSideProps

3. Static Site Generation (SSG):
   - HTML generated at build time
   - Fastest performance
   - Best for static content
   - Example: Next.js with getStaticProps

4. Incremental Static Regeneration (ISR):
   - Static pages updated on-demand
   - Best of SSG and SSR
   - Example: Next.js with revalidate

5. Hybrid Rendering:
   - Mix of CSR, SSR, SSG per route
   - Modern frameworks support this
*/
