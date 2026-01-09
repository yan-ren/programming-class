import { useState, useEffect, useCallback } from 'react';
import type { Todo, FetchResult } from '../types';

// ============================================================
// DATA FETCHING DEMO
// Covers: Fetch API, loading states, error handling, TypeScript types
// ============================================================

export function DataFetchingDemo() {
  // Type-safe state using discriminated union
  const [todosResult, setTodosResult] = useState<FetchResult<Todo[]>>({ status: 'idle' });
  const [newTodoTitle, setNewTodoTitle] = useState('');

  // ============================================================
  // FETCH DATA - Using Fetch API with proper error handling
  // ============================================================
  const fetchTodos = useCallback(async () => {
    setTodosResult({ status: 'loading' });

    try {
      const response = await fetch('/api/todos');

      // Check if response is OK (status 200-299)
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      // Parse JSON with type assertion
      const data: Todo[] = await response.json();

      setTodosResult({ status: 'success', data });
    } catch (error) {
      // Handle different error types
      const message = error instanceof Error ? error.message : 'Unknown error';
      setTodosResult({ status: 'error', error: message });
    }
  }, []);

  // ============================================================
  // CREATE TODO - POST request example
  // ============================================================
  const createTodo = async () => {
    if (!newTodoTitle.trim()) return;

    try {
      const response = await fetch('/api/todos', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ title: newTodoTitle }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      // Refetch to update list
      setNewTodoTitle('');
      fetchTodos();
    } catch (error) {
      console.error('Failed to create todo:', error);
    }
  };

  // ============================================================
  // TOGGLE TODO - PATCH request example
  // ============================================================
  const toggleTodo = async (todo: Todo) => {
    try {
      const response = await fetch(`/api/todos/${todo.id}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ completed: !todo.completed }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      fetchTodos();
    } catch (error) {
      console.error('Failed to toggle todo:', error);
    }
  };

  // ============================================================
  // DELETE TODO - DELETE request example
  // ============================================================
  const deleteTodo = async (id: string) => {
    try {
      const response = await fetch(`/api/todos/${id}`, {
        method: 'DELETE',
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      fetchTodos();
    } catch (error) {
      console.error('Failed to delete todo:', error);
    }
  };

  // Fetch on mount
  useEffect(() => {
    fetchTodos();
  }, [fetchTodos]);

  return (
    <div className="space-y-8">
      <section className="bg-white p-6 rounded-lg shadow">
        <h2 className="text-xl font-bold mb-4">Data Fetching with Fetch API</h2>

        {/* Create Todo Form */}
        <div className="mb-6 p-4 bg-blue-50 rounded">
          <h3 className="font-semibold mb-2">Create Todo (POST)</h3>
          <div className="flex gap-2">
            <input
              type="text"
              value={newTodoTitle}
              onChange={(e) => setNewTodoTitle(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && createTodo()}
              className="flex-1 px-3 py-2 border rounded"
              placeholder="Enter todo title..."
            />
            <button
              onClick={createTodo}
              className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
            >
              Add Todo
            </button>
          </div>
        </div>

        {/* Todos List with Loading/Error States */}
        <div className="mb-6 p-4 bg-green-50 rounded">
          <div className="flex justify-between items-center mb-2">
            <h3 className="font-semibold">Todo List (GET)</h3>
            <button
              onClick={fetchTodos}
              className="px-3 py-1 bg-green-500 text-white rounded text-sm hover:bg-green-600"
            >
              Refresh
            </button>
          </div>

          {/* Render based on fetch status */}
          {todosResult.status === 'idle' && (
            <p className="text-gray-500">Click refresh to load todos</p>
          )}

          {todosResult.status === 'loading' && (
            <div className="flex items-center gap-2 text-blue-600">
              <svg className="animate-spin h-5 w-5" viewBox="0 0 24 24">
                <circle
                  className="opacity-25"
                  cx="12"
                  cy="12"
                  r="10"
                  stroke="currentColor"
                  strokeWidth="4"
                  fill="none"
                />
                <path
                  className="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"
                />
              </svg>
              <span>Loading...</span>
            </div>
          )}

          {todosResult.status === 'error' && (
            <div className="p-3 bg-red-100 text-red-700 rounded">
              <p>Error: {todosResult.error}</p>
              <p className="text-sm mt-1">Make sure the backend is running on port 3001</p>
            </div>
          )}

          {todosResult.status === 'success' && (
            <ul className="space-y-2">
              {todosResult.data.map((todo) => (
                <li
                  key={todo.id}
                  className="flex items-center justify-between p-2 bg-white rounded"
                >
                  <div className="flex items-center gap-2">
                    <input
                      type="checkbox"
                      checked={todo.completed}
                      onChange={() => toggleTodo(todo)}
                      className="h-4 w-4"
                    />
                    <span className={todo.completed ? 'line-through text-gray-400' : ''}>
                      {todo.title}
                    </span>
                  </div>
                  <button
                    onClick={() => deleteTodo(todo.id)}
                    className="text-red-500 hover:text-red-700 text-sm"
                  >
                    Delete
                  </button>
                </li>
              ))}
            </ul>
          )}
        </div>

        {/* Code Example */}
        <div className="p-4 bg-gray-900 text-green-400 rounded font-mono text-sm overflow-x-auto">
          <pre>{`// Type-safe fetch with explicit types
const fetchTodos = async (): Promise<void> => {
  setResult({ status: 'loading' });
  
  try {
    const response = await fetch('/api/todos');
    
    if (!response.ok) {
      throw new Error(\`HTTP error! status: \${response.status}\`);
    }
    
    const data: Todo[] = await response.json();
    setResult({ status: 'success', data });
  } catch (error) {
    const message = error instanceof Error 
      ? error.message 
      : 'Unknown error';
    setResult({ status: 'error', error: message });
  }
};`}</pre>
        </div>

        {/* Key Concepts */}
        <div className="mt-4 p-4 bg-yellow-50 border border-yellow-200 rounded">
          <h3 className="font-semibold mb-2">Fetch API Key Points</h3>
          <ul className="text-sm space-y-1">
            <li>• <strong>fetch()</strong> returns a Promise that resolves to Response</li>
            <li>• <strong>response.ok</strong> is true for status 200-299</li>
            <li>• <strong>response.json()</strong> returns a Promise with parsed data</li>
            <li>• <strong>fetch doesn&apos;t reject</strong> on HTTP errors (only network errors)</li>
            <li>• Always handle loading, success, and error states</li>
            <li>• Use TypeScript types for type-safe data handling</li>
          </ul>
        </div>
      </section>
    </div>
  );
}
