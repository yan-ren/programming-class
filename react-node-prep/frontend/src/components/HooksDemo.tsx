import { useState, useEffect, useCallback, useMemo, useRef, useReducer } from 'react';

// ============================================================
// HOOKS & STATE MANAGEMENT DEMO
// Covers: useState, useEffect, useCallback, useMemo, useRef, useReducer
// ============================================================

interface CounterState {
  count: number;
  step: number;
}

type CounterAction =
  | { type: 'increment' }
  | { type: 'decrement' }
  | { type: 'setStep'; payload: number }
  | { type: 'reset' };

function counterReducer(state: CounterState, action: CounterAction): CounterState {
  switch (action.type) {
    case 'increment':
      return { ...state, count: state.count + state.step };
    case 'decrement':
      return { ...state, count: state.count - state.step };
    case 'setStep':
      return { ...state, step: action.payload };
    case 'reset':
      return { count: 0, step: 1 };
    default:
      return state;
  }
}

export function HooksDemo() {
  // ============================================================
  // useState - Basic state management
  // ============================================================
  const [count, setCount] = useState<number>(0);
  const [items, setItems] = useState<string[]>(['Item 1', 'Item 2']);
  const [inputValue, setInputValue] = useState('');

  // ============================================================
  // useReducer - Complex state logic
  // Better for: complex state transitions, multiple sub-values
  // ============================================================
  const [state, dispatch] = useReducer(counterReducer, { count: 0, step: 1 });

  // ============================================================
  // useRef - Mutable value that persists across renders
  // Does NOT trigger re-render when changed
  // ============================================================
  const renderCount = useRef(0);
  const inputRef = useRef<HTMLInputElement>(null);

  // Track renders
  useEffect(() => {
    renderCount.current += 1;
  });

  // ============================================================
  // useMemo - Memoize expensive computations
  // Only recomputes when dependencies change
  // ============================================================
  const expensiveCalculation = useMemo(() => {
    console.log('Computing expensive value...');
    // Simulate expensive operation
    let result = 0;
    for (let i = 0; i < count * 1000; i++) {
      result += i;
    }
    return result;
  }, [count]); // Only recompute when count changes

  // ============================================================
  // DERIVED STATE - Compute from existing state instead of storing
  // ============================================================
  // GOOD: Derive the value
  const itemCount = items.length;
  const hasItems = items.length > 0;

  // BAD: Don't do this - storing derived state
  // const [itemCount, setItemCount] = useState(items.length);
  // useEffect(() => setItemCount(items.length), [items]);

  // ============================================================
  // useCallback - Memoize functions
  // Prevents function recreation on each render
  // ============================================================
  const handleAddItem = useCallback(() => {
    if (inputValue.trim()) {
      setItems(prev => [...prev, inputValue.trim()]);
      setInputValue('');
    }
  }, [inputValue]); // Only recreate when inputValue changes

  const handleRemoveItem = useCallback((index: number) => {
    setItems(prev => prev.filter((_, i) => i !== index));
  }, []); // Never recreates - no dependencies

  // Focus input using ref
  const focusInput = useCallback(() => {
    inputRef.current?.focus();
  }, []);

  return (
    <div className="space-y-8">
      <section className="bg-white p-6 rounded-lg shadow">
        <h2 className="text-xl font-bold mb-4">Hooks & State Management</h2>
        <p className="text-gray-600 mb-4">
          Render count: <span className="font-mono bg-gray-100 px-2 py-1">{renderCount.current}</span>
        </p>

        {/* useState Demo */}
        <div className="mb-6 p-4 bg-blue-50 rounded">
          <h3 className="font-semibold mb-2">useState - Simple Counter</h3>
          <div className="flex items-center gap-4">
            <button
              onClick={() => setCount(c => c - 1)}
              className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
            >
              -
            </button>
            <span className="text-2xl font-bold">{count}</span>
            <button
              onClick={() => setCount(c => c + 1)}
              className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
            >
              +
            </button>
          </div>
          <p className="text-sm text-gray-600 mt-2">
            Expensive calculation result: {expensiveCalculation}
          </p>
        </div>

        {/* useReducer Demo */}
        <div className="mb-6 p-4 bg-green-50 rounded">
          <h3 className="font-semibold mb-2">useReducer - Counter with Step</h3>
          <div className="flex items-center gap-4 mb-2">
            <button
              onClick={() => dispatch({ type: 'decrement' })}
              className="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600"
            >
              - {state.step}
            </button>
            <span className="text-2xl font-bold">{state.count}</span>
            <button
              onClick={() => dispatch({ type: 'increment' })}
              className="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600"
            >
              + {state.step}
            </button>
            <button
              onClick={() => dispatch({ type: 'reset' })}
              className="px-3 py-2 bg-gray-500 text-white rounded hover:bg-gray-600"
            >
              Reset
            </button>
          </div>
          <div className="flex items-center gap-2">
            <label className="text-sm">Step:</label>
            <input
              type="number"
              value={state.step}
              onChange={(e) => dispatch({ type: 'setStep', payload: Number(e.target.value) })}
              className="w-20 px-2 py-1 border rounded"
              min="1"
            />
          </div>
        </div>

        {/* useRef + Derived State Demo */}
        <div className="mb-6 p-4 bg-purple-50 rounded">
          <h3 className="font-semibold mb-2">useRef + Derived State - Item List</h3>
          <div className="flex gap-2 mb-4">
            <input
              ref={inputRef}
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && handleAddItem()}
              className="flex-1 px-3 py-2 border rounded"
              placeholder="Add item..."
            />
            <button
              onClick={handleAddItem}
              className="px-4 py-2 bg-purple-500 text-white rounded hover:bg-purple-600"
            >
              Add
            </button>
            <button
              onClick={focusInput}
              className="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600"
            >
              Focus
            </button>
          </div>
          
          <p className="text-sm text-gray-600 mb-2">
            Item count (derived): {itemCount} | Has items: {hasItems ? 'Yes' : 'No'}
          </p>
          
          <ul className="space-y-1">
            {items.map((item, index) => (
              <li key={index} className="flex justify-between items-center bg-white p-2 rounded">
                <span>{item}</span>
                <button
                  onClick={() => handleRemoveItem(index)}
                  className="text-red-500 hover:text-red-700"
                >
                  Remove
                </button>
              </li>
            ))}
          </ul>
        </div>

        {/* Key Concepts Box */}
        <div className="p-4 bg-yellow-50 border border-yellow-200 rounded">
          <h3 className="font-semibold mb-2">Key Concepts</h3>
          <ul className="text-sm space-y-1">
            <li>• <strong>useState</strong>: Simple state, triggers re-render on change</li>
            <li>• <strong>useReducer</strong>: Complex state with multiple actions</li>
            <li>• <strong>useMemo</strong>: Cache expensive calculations</li>
            <li>• <strong>useCallback</strong>: Cache function references</li>
            <li>• <strong>useRef</strong>: Mutable value, no re-render on change</li>
            <li>• <strong>Derived State</strong>: Compute from state, don&apos;t store redundantly</li>
          </ul>
        </div>
      </section>
    </div>
  );
}
