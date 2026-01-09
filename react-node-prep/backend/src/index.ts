import express, { Request, Response, NextFunction } from 'express';
import cors from 'cors';
import { authRouter } from './routes/auth';
import { todosRouter } from './routes/todos';
import { usersRouter } from './routes/users';
import { errorHandler, AppError } from './middleware/errorHandler';
import { rateLimiter } from './middleware/rateLimiter';

const app = express();
const PORT = process.env.PORT || 3001;

// Middleware
app.use(cors());
app.use(express.json());

// Rate limiting for spiky traffic - demonstrates handling uneven load
app.use(rateLimiter);

// Routes
app.use('/api/auth', authRouter);
app.use('/api/todos', todosRouter);
app.use('/api/users', usersRouter);

// Health check endpoint
app.get('/api/health', (req: Request, res: Response) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// ============================================================
// ERROR HANDLING CONCEPTS - Key Assessment Topic
// ============================================================

// 1. Synchronous error example
app.get('/api/sync-error', (req: Request, res: Response) => {
  // Sync errors are caught by Express automatically
  throw new AppError('This is a synchronous error', 400);
});

// 2. Async/await error example (needs try-catch or error handler wrapper)
app.get('/api/async-error', async (req: Request, res: Response, next: NextFunction) => {
  try {
    await simulateAsyncOperation();
    res.json({ success: true });
  } catch (error) {
    // Pass to error handler middleware
    next(error);
  }
});

// 3. Promise rejection (uncaught - dangerous!)
app.get('/api/promise-error', (req: Request, res: Response, next: NextFunction) => {
  simulatePromiseRejection()
    .then(() => res.json({ success: true }))
    .catch(next); // Always handle promise rejections!
});

// 4. Callback-style error (legacy pattern)
app.get('/api/callback-error', (req: Request, res: Response, next: NextFunction) => {
  simulateCallbackOperation((error, result) => {
    if (error) {
      return next(error);
    }
    res.json(result);
  });
});

// Helper functions for error demonstrations
async function simulateAsyncOperation(): Promise<void> {
  throw new AppError('Async operation failed', 500);
}

function simulatePromiseRejection(): Promise<void> {
  return Promise.reject(new AppError('Promise rejected', 500));
}

function simulateCallbackOperation(
  callback: (error: Error | null, result?: object) => void
): void {
  setTimeout(() => {
    callback(new AppError('Callback operation failed', 500));
  }, 100);
}

// Global error handler - MUST be last middleware
app.use(errorHandler);

// Handle uncaught exceptions (process-level)
process.on('uncaughtException', (error: Error) => {
  console.error('Uncaught Exception:', error);
  // In production: log, alert, then gracefully shutdown
  process.exit(1);
});

// Handle unhandled promise rejections (process-level)
process.on('unhandledRejection', (reason: unknown) => {
  console.error('Unhandled Rejection:', reason);
  // In production: log and potentially restart
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
  console.log('Available endpoints:');
  console.log('  GET  /api/health');
  console.log('  POST /api/auth/login');
  console.log('  GET  /api/auth/profile (requires JWT)');
  console.log('  GET  /api/todos');
  console.log('  POST /api/todos');
  console.log('  GET  /api/users');
  console.log('  GET  /api/users/:id');
});
