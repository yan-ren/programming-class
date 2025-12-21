import { Router, Request, Response } from 'express';
import { authenticate, generateToken, AuthenticatedRequest } from '../middleware/auth';
import { AppError } from '../middleware/errorHandler';

export const authRouter = Router();

// Mock user database
const users = [
  { id: '1', email: 'user@example.com', password: 'password123' },
];

// ============================================================
// LOGIN ENDPOINT
// ============================================================

interface LoginBody {
  email: string;
  password: string;
}

authRouter.post('/login', (req: Request<{}, {}, LoginBody>, res: Response) => {
  const { email, password } = req.body;

  if (!email || !password) {
    throw new AppError('Email and password are required', 400);
  }

  const user = users.find(u => u.email === email && u.password === password);

  if (!user) {
    throw new AppError('Invalid credentials', 401);
  }

  const token = generateToken({ id: user.id, email: user.email });

  res.json({
    token,
    user: { id: user.id, email: user.email },
  });
});

// ============================================================
// PROTECTED ROUTE EXAMPLE
// ============================================================

authRouter.get('/profile', authenticate, (req: AuthenticatedRequest, res: Response) => {
  res.json({
    message: 'This is a protected route',
    user: req.user,
  });
});
