import { Request, Response, NextFunction } from 'express';
import jwt from 'jsonwebtoken';
import { AppError } from './errorHandler';

// ============================================================
// AUTHENTICATION CONCEPTS
// ============================================================

// Secret key (in production, use environment variable)
const JWT_SECRET = process.env.JWT_SECRET || 'your-secret-key-change-in-production';

// Extend Express Request type to include user
export interface AuthenticatedRequest extends Request {
  user?: {
    id: string;
    email: string;
  };
}

// ============================================================
// JWT AUTHENTICATION MIDDLEWARE
// ============================================================

export const authenticate = (
  req: AuthenticatedRequest,
  res: Response,
  next: NextFunction
): void => {
  // Get token from Authorization header
  const authHeader = req.headers.authorization;
  
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    throw new AppError('No token provided', 401);
  }

  const token = authHeader.split(' ')[1];

  try {
    // Verify token
    const decoded = jwt.verify(token, JWT_SECRET) as { id: string; email: string };
    req.user = decoded;
    next();
  } catch (error) {
    if (error instanceof jwt.TokenExpiredError) {
      throw new AppError('Token expired', 401);
    }
    if (error instanceof jwt.JsonWebTokenError) {
      throw new AppError('Invalid token', 401);
    }
    throw error;
  }
};

// Helper to generate JWT
export const generateToken = (payload: { id: string; email: string }): string => {
  return jwt.sign(payload, JWT_SECRET, { expiresIn: '1h' });
};

// ============================================================
// AUTHENTICATION MODELS (Verbal Discussion Notes)
// ============================================================

/*
1. SESSION-BASED AUTHENTICATION:
   - Server stores session data (in memory, database, or Redis)
   - Client receives session ID in cookie
   - Pros: Easy revocation, server control
   - Cons: Stateful, harder to scale horizontally

2. TOKEN-BASED (JWT) AUTHENTICATION:
   - Server issues signed token containing user info
   - Client stores token (localStorage, cookie)
   - Pros: Stateless, scalable, works across domains
   - Cons: Can't easily revoke, larger payload

3. OAUTH 2.0:
   - Delegated authorization protocol
   - Third-party authentication (Google, GitHub, etc.)
   - Uses access tokens and refresh tokens
   - Common flows: Authorization Code, Client Credentials, Implicit

4. API KEYS:
   - Simple static key for service-to-service auth
   - Not suitable for user authentication
   - Easy to implement, but limited security

5. BASIC AUTH:
   - Username:password in header (base64 encoded)
   - Simple but requires HTTPS
   - Not suitable for browsers (no logout)

BEST PRACTICES:
- Always use HTTPS
- Store tokens securely (httpOnly cookies when possible)
- Implement token refresh mechanisms
- Use short-lived access tokens
- Implement proper logout (token blacklist for JWT)
*/
