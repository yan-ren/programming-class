import { Request, Response, NextFunction } from 'express';

// ============================================================
// RATE LIMITING - Handling Spiky Traffic
// ============================================================

interface RateLimitEntry {
  count: number;
  startTime: number;
}

// Simple in-memory rate limiter (use Redis in production for distributed systems)
const requestCounts: Map<string, RateLimitEntry> = new Map();

// Configuration
const WINDOW_SIZE_MS = 60 * 1000; // 1 minute window
const MAX_REQUESTS = 100; // Max requests per window

export const rateLimiter = (
  req: Request,
  res: Response,
  next: NextFunction
): void => {
  // Get client identifier (IP address or user ID for authenticated requests)
  const clientId = req.ip || 'unknown';
  const now = Date.now();

  // Get or create entry for this client
  let entry = requestCounts.get(clientId);

  if (!entry || now - entry.startTime > WINDOW_SIZE_MS) {
    // Start new window
    entry = { count: 1, startTime: now };
    requestCounts.set(clientId, entry);
  } else {
    entry.count++;
  }

  // Set rate limit headers
  res.setHeader('X-RateLimit-Limit', MAX_REQUESTS);
  res.setHeader('X-RateLimit-Remaining', Math.max(0, MAX_REQUESTS - entry.count));
  res.setHeader('X-RateLimit-Reset', entry.startTime + WINDOW_SIZE_MS);

  if (entry.count > MAX_REQUESTS) {
    res.status(429).json({
      error: {
        message: 'Too many requests. Please try again later.',
        retryAfter: Math.ceil((entry.startTime + WINDOW_SIZE_MS - now) / 1000),
      },
    });
    return;
  }

  next();
};

// ============================================================
// SCALING CONCEPTS (Comments for verbal discussion)
// ============================================================

/*
HORIZONTAL vs VERTICAL SCALING:

1. Vertical Scaling (Scale Up):
   - Add more CPU, RAM, storage to existing server
   - Simpler but has limits
   - Single point of failure

2. Horizontal Scaling (Scale Out):
   - Add more servers/instances
   - Better for handling spiky traffic
   - Requires: stateless services, shared sessions, load balancing

ELASTIC COMPUTE OPTIONS:

1. Auto-scaling Groups (AWS ASG, GCP Instance Groups):
   - Automatically add/remove instances based on metrics
   - Configure min/max instances and scaling policies
   - Good for predictable patterns

2. Serverless (AWS Lambda, GCP Cloud Functions):
   - Scales to zero when not in use
   - Automatic scaling per request
   - Cold start latency tradeoff
   - Best for variable/unpredictable traffic

3. Container Orchestration (Kubernetes):
   - Horizontal Pod Autoscaler (HPA)
   - Fine-grained control over scaling
   - More operational complexity

HANDLING SPIKY TRAFFIC:

1. Rate Limiting (implemented above)
   - Protect backend from overload
   - Fair distribution of resources

2. Request Queuing:
   - Queue requests during spikes
   - Process at sustainable rate
   - Use message queues (RabbitMQ, SQS)

3. Circuit Breaker Pattern:
   - Fail fast when downstream services are down
   - Prevent cascade failures

4. Caching:
   - Reduce backend load
   - Serve common requests from cache

5. CDN:
   - Edge caching for static content
   - Reduces origin server load
*/
