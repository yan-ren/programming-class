import { useState, useCallback, useRef, useEffect } from 'react';

// ============================================================
// DEBOUNCE & THROTTLE DEMO
// Controlling high-frequency browser events
// ============================================================

// ============================================================
// CUSTOM HOOKS FOR DEBOUNCE AND THROTTLE
// ============================================================

// Debounce hook - delays execution until after wait time with no new calls
function useDebounce<T extends (...args: Parameters<T>) => void>(
  callback: T,
  delay: number
): T {
  const timeoutRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  const debouncedCallback = useCallback(
    (...args: Parameters<T>) => {
      if (timeoutRef.current) {
        clearTimeout(timeoutRef.current);
      }
      timeoutRef.current = setTimeout(() => {
        callback(...args);
      }, delay);
    },
    [callback, delay]
  ) as T;

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      if (timeoutRef.current) {
        clearTimeout(timeoutRef.current);
      }
    };
  }, []);

  return debouncedCallback;
}

// Throttle hook - limits execution to at most once per interval
function useThrottle<T extends (...args: Parameters<T>) => void>(
  callback: T,
  limit: number
): T {
  const lastRanRef = useRef<number>(0);
  const timeoutRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  const throttledCallback = useCallback(
    (...args: Parameters<T>) => {
      const now = Date.now();

      if (now - lastRanRef.current >= limit) {
        callback(...args);
        lastRanRef.current = now;
      } else {
        // Schedule trailing call
        if (timeoutRef.current) {
          clearTimeout(timeoutRef.current);
        }
        timeoutRef.current = setTimeout(() => {
          callback(...args);
          lastRanRef.current = Date.now();
        }, limit - (now - lastRanRef.current));
      }
    },
    [callback, limit]
  ) as T;

  useEffect(() => {
    return () => {
      if (timeoutRef.current) {
        clearTimeout(timeoutRef.current);
      }
    };
  }, []);

  return throttledCallback;
}

// Debounced value hook - common pattern for search inputs
function useDebouncedValue<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState<T>(value);

  useEffect(() => {
    const timeout = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => clearTimeout(timeout);
  }, [value, delay]);

  return debouncedValue;
}

export function DebounceThrottleDemo() {
  // Raw input states
  const [searchInput, setSearchInput] = useState('');
  const [scrollY, setScrollY] = useState(0);

  // Counters to show call frequency
  const [rawCount, setRawCount] = useState(0);
  const [debouncedCount, setDebouncedCount] = useState(0);
  const [throttledCount, setThrottledCount] = useState(0);

  // Search results state
  const [searchResults, setSearchResults] = useState<string[]>([]);

  // Debounced search value
  const debouncedSearch = useDebouncedValue(searchInput, 500);

  // ============================================================
  // DEBOUNCED SEARCH - Only fires after user stops typing
  // ============================================================
  useEffect(() => {
    if (debouncedSearch) {
      // Simulate API search
      const mockResults = [
        `Result for "${debouncedSearch}" - 1`,
        `Result for "${debouncedSearch}" - 2`,
        `Result for "${debouncedSearch}" - 3`,
      ];
      setSearchResults(mockResults);
      setDebouncedCount(c => c + 1);
    } else {
      setSearchResults([]);
    }
  }, [debouncedSearch]);

  // ============================================================
  // RAW INPUT HANDLER - Fires on every keystroke
  // ============================================================
  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setSearchInput(e.target.value);
    setRawCount(c => c + 1);
  };

  // ============================================================
  // THROTTLED SCROLL HANDLER - Good for scroll/resize events
  // ============================================================
  const handleScroll = useCallback(() => {
    setScrollY(window.scrollY);
  }, []);

  const throttledScroll = useThrottle(handleScroll, 100);

  useEffect(() => {
    const onScroll = () => {
      throttledScroll();
      setThrottledCount(c => c + 1);
    };

    window.addEventListener('scroll', onScroll);
    return () => window.removeEventListener('scroll', onScroll);
  }, [throttledScroll]);

  return (
    <div className="space-y-8">
      <section className="bg-white p-6 rounded-lg shadow">
        <h2 className="text-xl font-bold mb-4">Debounce & Throttle</h2>

        {/* Counter Display */}
        <div className="mb-6 grid grid-cols-3 gap-4">
          <div className="p-4 bg-red-50 rounded text-center">
            <p className="text-2xl font-bold text-red-600">{rawCount}</p>
            <p className="text-sm text-gray-600">Raw Input Events</p>
          </div>
          <div className="p-4 bg-green-50 rounded text-center">
            <p className="text-2xl font-bold text-green-600">{debouncedCount}</p>
            <p className="text-sm text-gray-600">Debounced Calls</p>
          </div>
          <div className="p-4 bg-blue-50 rounded text-center">
            <p className="text-2xl font-bold text-blue-600">{throttledCount}</p>
            <p className="text-sm text-gray-600">Throttled Calls</p>
          </div>
        </div>

        {/* Debounced Search Demo */}
        <div className="mb-6 p-4 bg-green-50 rounded">
          <h3 className="font-semibold mb-2">Debounced Search (500ms)</h3>
          <p className="text-sm text-gray-600 mb-2">
            Type quickly - search only fires after you stop typing for 500ms
          </p>
          <input
            type="text"
            value={searchInput}
            onChange={handleInputChange}
            className="w-full px-3 py-2 border rounded mb-2"
            placeholder="Search..."
          />
          <div className="text-sm">
            <p>Input value: &quot;{searchInput}&quot;</p>
            <p>Debounced value: &quot;{debouncedSearch}&quot;</p>
          </div>
          {searchResults.length > 0 && (
            <ul className="mt-2 space-y-1">
              {searchResults.map((result, i) => (
                <li key={i} className="p-2 bg-white rounded text-sm">
                  {result}
                </li>
              ))}
            </ul>
          )}
        </div>

        {/* Throttle Info */}
        <div className="mb-6 p-4 bg-blue-50 rounded">
          <h3 className="font-semibold mb-2">Throttled Scroll (100ms)</h3>
          <p className="text-sm text-gray-600 mb-2">
            Scroll the page - handler fires at most once per 100ms
          </p>
          <p className="font-mono bg-white p-2 rounded">
            window.scrollY: {scrollY}px
          </p>
        </div>

        {/* Comparison */}
        <div className="mb-6 p-4 bg-purple-50 rounded">
          <h3 className="font-semibold mb-2">Debounce vs Throttle</h3>
          <div className="grid grid-cols-2 gap-4 text-sm">
            <div>
              <h4 className="font-medium text-purple-700">Debounce</h4>
              <ul className="space-y-1 mt-1">
                <li>• Waits until activity stops</li>
                <li>• Fires once after delay</li>
                <li>• Good for: search input, form validation</li>
                <li>• Example: autocomplete</li>
              </ul>
            </div>
            <div>
              <h4 className="font-medium text-purple-700">Throttle</h4>
              <ul className="space-y-1 mt-1">
                <li>• Fires at regular intervals</li>
                <li>• Limits frequency of calls</li>
                <li>• Good for: scroll, resize, mousemove</li>
                <li>• Example: infinite scroll</li>
              </ul>
            </div>
          </div>
        </div>

        {/* Code Example */}
        <div className="p-4 bg-gray-900 text-green-400 rounded font-mono text-sm overflow-x-auto">
          <pre>{`// Debounce implementation
function debounce<T extends (...args: any[]) => void>(
  fn: T, 
  delay: number
): T {
  let timeoutId: ReturnType<typeof setTimeout>;
  
  return ((...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => fn(...args), delay);
  }) as T;
}

// Throttle implementation
function throttle<T extends (...args: any[]) => void>(
  fn: T, 
  limit: number
): T {
  let lastRan = 0;
  
  return ((...args) => {
    const now = Date.now();
    if (now - lastRan >= limit) {
      fn(...args);
      lastRan = now;
    }
  }) as T;
}`}</pre>
        </div>

        {/* Reset Button */}
        <div className="mt-4">
          <button
            onClick={() => {
              setRawCount(0);
              setDebouncedCount(0);
              setThrottledCount(0);
              setSearchInput('');
              setSearchResults([]);
            }}
            className="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600"
          >
            Reset Counters
          </button>
        </div>
      </section>
    </div>
  );
}
