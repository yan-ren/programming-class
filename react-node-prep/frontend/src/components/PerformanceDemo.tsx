import { useState, useCallback, memo, useMemo } from 'react';

// ============================================================
// PERFORMANCE OPTIMIZATION DEMO
// Covers: React.memo, useCallback, useMemo, avoiding unnecessary renders
// ============================================================

// ============================================================
// React.memo - Skip re-rendering when props haven't changed
// ============================================================
interface ExpensiveChildProps {
  value: number;
  onClick: () => void;
}

// WITHOUT memo - re-renders on every parent render
const ExpensiveChildWithoutMemo = ({ value, onClick }: ExpensiveChildProps) => {
  console.log('ExpensiveChildWithoutMemo rendered');
  // Simulate expensive render
  const startTime = performance.now();
  while (performance.now() - startTime < 5) {
    // Artificial delay
  }
  return (
    <div className="p-3 bg-red-100 rounded">
      <span>Without memo: {value}</span>
      <button onClick={onClick} className="ml-2 px-2 py-1 bg-red-500 text-white rounded text-sm">
        Click
      </button>
    </div>
  );
};

// WITH memo - only re-renders when props change
const ExpensiveChildWithMemo = memo(({ value, onClick }: ExpensiveChildProps) => {
  console.log('ExpensiveChildWithMemo rendered');
  const startTime = performance.now();
  while (performance.now() - startTime < 5) {
    // Artificial delay
  }
  return (
    <div className="p-3 bg-green-100 rounded">
      <span>With memo: {value}</span>
      <button onClick={onClick} className="ml-2 px-2 py-1 bg-green-500 text-white rounded text-sm">
        Click
      </button>
    </div>
  );
});

ExpensiveChildWithMemo.displayName = 'ExpensiveChildWithMemo';

// ============================================================
// List Optimization Example
// ============================================================
interface ListItemProps {
  item: { id: number; name: string };
  onSelect: (id: number) => void;
}

const ListItem = memo(({ item, onSelect }: ListItemProps) => {
  console.log(`ListItem ${item.id} rendered`);
  return (
    <li
      className="p-2 bg-white rounded cursor-pointer hover:bg-gray-50"
      onClick={() => onSelect(item.id)}
    >
      {item.name}
    </li>
  );
});

ListItem.displayName = 'ListItem';

export function PerformanceDemo() {
  const [count, setCount] = useState(0);
  const [childValue, setChildValue] = useState(100);
  const [selectedId, setSelectedId] = useState<number | null>(null);

  // ============================================================
  // useCallback - Stabilize function reference
  // Without this, memo'd components receive new function on each render
  // ============================================================
  
  // BAD: Creates new function every render, breaks memo
  const handleClickUnstable = () => {
    console.log('Unstable click');
  };

  // GOOD: Stable function reference
  const handleClickStable = useCallback(() => {
    console.log('Stable click');
  }, []);

  // For list items - stable callback
  const handleSelectItem = useCallback((id: number) => {
    setSelectedId(id);
  }, []);

  // ============================================================
  // useMemo - Memoize expensive data transformations
  // ============================================================
  const items = useMemo(() => {
    console.log('Creating items array');
    return Array.from({ length: 5 }, (_, i) => ({
      id: i + 1,
      name: `Item ${i + 1}`,
    }));
  }, []); // Empty deps = only create once

  // Filtered items - recalculates only when items or selectedId changes
  const filteredInfo = useMemo(() => {
    console.log('Computing filtered info');
    return {
      selected: items.find(i => i.id === selectedId),
      count: items.length,
    };
  }, [items, selectedId]);

  return (
    <div className="space-y-8">
      <section className="bg-white p-6 rounded-lg shadow">
        <h2 className="text-xl font-bold mb-4">Performance Optimization</h2>

        {/* Parent Re-render Trigger */}
        <div className="mb-6 p-4 bg-gray-100 rounded">
          <h3 className="font-semibold mb-2">Parent State (triggers re-render)</h3>
          <div className="flex items-center gap-4">
            <button
              onClick={() => setCount(c => c + 1)}
              className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
            >
              Update Parent Count: {count}
            </button>
            <button
              onClick={() => setChildValue(v => v + 1)}
              className="px-4 py-2 bg-purple-500 text-white rounded hover:bg-purple-600"
            >
              Update Child Value: {childValue}
            </button>
          </div>
          <p className="text-sm text-gray-600 mt-2">
            Open console to see which components re-render
          </p>
        </div>

        {/* React.memo Comparison */}
        <div className="mb-6 p-4 bg-blue-50 rounded">
          <h3 className="font-semibold mb-2">React.memo Comparison</h3>
          <div className="space-y-2">
            <ExpensiveChildWithoutMemo
              value={childValue}
              onClick={handleClickUnstable}
            />
            <ExpensiveChildWithMemo
              value={childValue}
              onClick={handleClickStable}
            />
          </div>
          <p className="text-sm text-gray-600 mt-2">
            Click &quot;Update Parent Count&quot; - only the red component re-renders!
          </p>
        </div>

        {/* useCallback for Lists */}
        <div className="mb-6 p-4 bg-green-50 rounded">
          <h3 className="font-semibold mb-2">Optimized List with useCallback</h3>
          <ul className="space-y-1">
            {items.map(item => (
              <ListItem
                key={item.id}
                item={item}
                onSelect={handleSelectItem}
              />
            ))}
          </ul>
          <p className="text-sm text-gray-600 mt-2">
            Selected: {filteredInfo.selected?.name || 'None'} (Total: {filteredInfo.count})
          </p>
        </div>

        {/* Key Concepts */}
        <div className="p-4 bg-yellow-50 border border-yellow-200 rounded">
          <h3 className="font-semibold mb-2">Performance Best Practices</h3>
          <ul className="text-sm space-y-1">
            <li>• <strong>React.memo</strong>: Wrap components that render often with same props</li>
            <li>• <strong>useCallback</strong>: Stabilize function references passed as props</li>
            <li>• <strong>useMemo</strong>: Cache expensive calculations and derived data</li>
            <li>• <strong>Keys</strong>: Use stable, unique keys for list items</li>
            <li>• <strong>Avoid</strong>: Creating new objects/arrays in render (e.g., style=&#123;&#123;&#125;&#125;)</li>
            <li>• <strong>Profile</strong>: Use React DevTools Profiler to identify bottlenecks</li>
          </ul>
        </div>

        {/* When NOT to Optimize */}
        <div className="mt-4 p-4 bg-red-50 border border-red-200 rounded">
          <h3 className="font-semibold mb-2">When NOT to Optimize</h3>
          <ul className="text-sm space-y-1">
            <li>• Don&apos;t memo everything - it has its own cost</li>
            <li>• Measure first - premature optimization is problematic</li>
            <li>• Simple components often don&apos;t benefit from memo</li>
            <li>• If props change frequently, memo won&apos;t help</li>
          </ul>
        </div>
      </section>
    </div>
  );
}
