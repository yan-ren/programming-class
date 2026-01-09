import { useState, useEffect, useRef } from 'react';

// ============================================================
// EFFECT LIFECYCLE DEMO
// Covers: useEffect lifecycle, cleanup, dependencies, common patterns
// ============================================================

export function EffectLifecycleDemo() {
  const [count, setCount] = useState(0);
  const [resourceId, setResourceId] = useState(1);
  const [isTimerRunning, setIsTimerRunning] = useState(false);
  const [timerValue, setTimerValue] = useState(0);
  const [windowWidth, setWindowWidth] = useState(window.innerWidth);
  const [logs, setLogs] = useState<string[]>([]);

  const mountTimeRef = useRef(Date.now());

  // Helper to add logs
  const addLog = (message: string) => {
    const elapsed = ((Date.now() - mountTimeRef.current) / 1000).toFixed(1);
    setLogs(prev => [...prev.slice(-9), `[${elapsed}s] ${message}`]);
  };

  // ============================================================
  // EFFECT 1: Run once on mount (empty deps)
  // ============================================================
  useEffect(() => {
    addLog('Component MOUNTED');

    // Cleanup runs on unmount
    return () => {
      console.log('Component UNMOUNTED');
    };
  }, []); // Empty array = only on mount

  // ============================================================
  // EFFECT 2: Run on every render (no deps array)
  // CAREFUL: This can cause performance issues
  // ============================================================
  // useEffect(() => {
  //   addLog('Rendered (no deps - runs every time)');
  // }); // No deps = runs every render

  // ============================================================
  // EFFECT 3: Run when specific dependency changes
  // ============================================================
  useEffect(() => {
    addLog(`Count changed to ${count}`);

    // Cleanup runs before next effect and on unmount
    return () => {
      addLog(`Cleaning up for count ${count}`);
    };
  }, [count]); // Only runs when count changes

  // ============================================================
  // EFFECT 4: Fetch data when resourceId changes (with cleanup)
  // ============================================================
  useEffect(() => {
    let isCancelled = false; // Prevent state update if component unmounts

    const fetchResource = async () => {
      addLog(`Fetching resource ${resourceId}...`);

      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 1000));

      if (!isCancelled) {
        addLog(`Resource ${resourceId} loaded`);
      } else {
        console.log(`Fetch for resource ${resourceId} was cancelled`);
      }
    };

    fetchResource();

    // Cleanup: cancel pending fetch
    return () => {
      isCancelled = true;
      addLog(`Cancelled fetch for resource ${resourceId}`);
    };
  }, [resourceId]);

  // ============================================================
  // EFFECT 5: Timer with cleanup (setInterval)
  // ============================================================
  useEffect(() => {
    if (!isTimerRunning) return;

    addLog('Timer STARTED');
    const intervalId = setInterval(() => {
      setTimerValue(v => v + 1);
    }, 1000);

    // Cleanup: clear interval
    return () => {
      clearInterval(intervalId);
      addLog('Timer STOPPED (cleanup)');
    };
  }, [isTimerRunning]); // Re-run when timer state changes

  // ============================================================
  // EFFECT 6: Event listener with cleanup
  // ============================================================
  useEffect(() => {
    const handleResize = () => {
      setWindowWidth(window.innerWidth);
    };

    window.addEventListener('resize', handleResize);
    addLog('Resize listener ADDED');

    // Cleanup: remove event listener
    return () => {
      window.removeEventListener('resize', handleResize);
      addLog('Resize listener REMOVED');
    };
  }, []); // Empty deps = setup once, cleanup on unmount

  return (
    <div className="space-y-8">
      <section className="bg-white p-6 rounded-lg shadow">
        <h2 className="text-xl font-bold mb-4">Effect Lifecycle</h2>

        {/* Effect Log */}
        <div className="mb-6 p-4 bg-gray-900 rounded">
          <h3 className="font-semibold mb-2 text-white">Effect Log</h3>
          <div className="font-mono text-sm text-green-400 h-48 overflow-y-auto">
            {logs.length === 0 ? (
              <p className="text-gray-500">No logs yet...</p>
            ) : (
              logs.map((log, i) => <p key={i}>{log}</p>)
            )}
          </div>
        </div>

        {/* Interactive Controls */}
        <div className="grid grid-cols-2 gap-4 mb-6">
          {/* Count Demo */}
          <div className="p-4 bg-blue-50 rounded">
            <h3 className="font-semibold mb-2">Dependency Change</h3>
            <p className="text-sm text-gray-600 mb-2">
              Effect runs when count changes, cleanup runs before
            </p>
            <button
              onClick={() => setCount(c => c + 1)}
              className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
            >
              Count: {count}
            </button>
          </div>

          {/* Resource Fetch Demo */}
          <div className="p-4 bg-green-50 rounded">
            <h3 className="font-semibold mb-2">Fetch with Cleanup</h3>
            <p className="text-sm text-gray-600 mb-2">
              Rapidly click to see fetch cancellation
            </p>
            <button
              onClick={() => setResourceId(id => id + 1)}
              className="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600"
            >
              Fetch Resource: {resourceId}
            </button>
          </div>

          {/* Timer Demo */}
          <div className="p-4 bg-purple-50 rounded">
            <h3 className="font-semibold mb-2">Interval with Cleanup</h3>
            <p className="text-sm text-gray-600 mb-2">
              Timer: {timerValue}s
            </p>
            <button
              onClick={() => setIsTimerRunning(r => !r)}
              className={`px-4 py-2 text-white rounded ${
                isTimerRunning
                  ? 'bg-red-500 hover:bg-red-600'
                  : 'bg-purple-500 hover:bg-purple-600'
              }`}
            >
              {isTimerRunning ? 'Stop Timer' : 'Start Timer'}
            </button>
          </div>

          {/* Window Size Demo */}
          <div className="p-4 bg-orange-50 rounded">
            <h3 className="font-semibold mb-2">Event Listener</h3>
            <p className="text-sm text-gray-600 mb-2">
              Resize window to see updates
            </p>
            <p className="font-mono bg-white p-2 rounded">
              Width: {windowWidth}px
            </p>
          </div>
        </div>

        {/* Key Concepts */}
        <div className="p-4 bg-yellow-50 border border-yellow-200 rounded">
          <h3 className="font-semibold mb-2">Effect Lifecycle Rules</h3>
          <ul className="text-sm space-y-1">
            <li>• <strong>Setup</strong> runs after render commits to DOM</li>
            <li>• <strong>Cleanup</strong> runs before next effect and on unmount</li>
            <li>• <strong>Empty deps []</strong>: run once on mount, cleanup on unmount</li>
            <li>• <strong>With deps [a, b]</strong>: run when a or b changes</li>
            <li>• <strong>No deps array</strong>: run after every render (avoid!)</li>
            <li>• Always cleanup: timers, subscriptions, event listeners</li>
            <li>• Use abort flags for async operations</li>
          </ul>
        </div>

        {/* Common Patterns */}
        <div className="mt-4 p-4 bg-gray-100 rounded">
          <h3 className="font-semibold mb-2">Common Effect Patterns</h3>
          <div className="grid grid-cols-2 gap-4 text-sm">
            <div>
              <h4 className="font-medium">Data Fetching</h4>
              <pre className="bg-white p-2 rounded mt-1 text-xs overflow-x-auto">{`useEffect(() => {
  let cancelled = false;
  
  fetchData().then(data => {
    if (!cancelled) setData(data);
  });
  
  return () => { cancelled = true; };
}, [id]);`}</pre>
            </div>
            <div>
              <h4 className="font-medium">Event Subscription</h4>
              <pre className="bg-white p-2 rounded mt-1 text-xs overflow-x-auto">{`useEffect(() => {
  const handler = (e) => { ... };
  
  window.addEventListener('resize', handler);
  
  return () => {
    window.removeEventListener('resize', handler);
  };
}, []);`}</pre>
            </div>
          </div>
        </div>

        {/* Clear Logs */}
        <div className="mt-4">
          <button
            onClick={() => {
              setLogs([]);
              mountTimeRef.current = Date.now();
            }}
            className="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600"
          >
            Clear Logs
          </button>
        </div>
      </section>
    </div>
  );
}
