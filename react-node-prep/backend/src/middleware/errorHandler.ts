import { Request, Response, NextFunction } from 'express';

// ============================================================
// CUSTOM ERROR CLASS
// ============================================================

export class AppError extends Error {
  statusCode: number;
  isOperational: boolean;

  constructor(message: string, statusCode: number = 500) {
    super(message);
    this.statusCode = statusCode;
    this.isOperational = true; // Distinguishes from programming errors
    
    // Maintains proper stack trace for where error was thrown
    Error.captureStackTrace(this, this.constructor);
  }
}

// ============================================================
// GLOBAL ERROR HANDLER MIDDLEWARE
// ============================================================

export const errorHandler = (
  err: Error | AppError,
  req: Request,
  res: Response,
  _next: NextFunction
): void => {
  // Default values
  let statusCode = 500;
  let message = 'Internal Server Error';
  
  // Check if it's our custom AppError
  if (err instanceof AppError) {
    statusCode = err.statusCode;
    message = err.message;
  } else if (err instanceof SyntaxError) {
    // Handle JSON parse errors
    statusCode = 400;
    message = 'Invalid JSON';
  }

  // Log the error (in production, use a proper logger)
  console.error(`[ERROR] ${statusCode} - ${message}`);
  console.error(err.stack);

  // Send response
  res.status(statusCode).json({
    error: {
      message,
      // Only include stack in development
      ...(process.env.NODE_ENV !== 'production' && { stack: err.stack }),
    },
  });
};

// ============================================================
// ASYNC HANDLER WRAPPER
// Automatically catches errors in async route handlers
// ============================================================

type AsyncHandler = (
  req: Request,
  res: Response,
  next: NextFunction
) => Promise<void>;

export const asyncHandler = (fn: AsyncHandler) => {
  return (req: Request, res: Response, next: NextFunction): void => {
    Promise.resolve(fn(req, res, next)).catch(next);
  };
};
