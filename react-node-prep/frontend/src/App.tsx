import { useState } from 'react';
import { HooksDemo } from './components/HooksDemo';
import { PerformanceDemo } from './components/PerformanceDemo';
import { DataFetchingDemo } from './components/DataFetchingDemo';
import { DebounceThrottleDemo } from './components/DebounceThrottleDemo';
import { EffectLifecycleDemo } from './components/EffectLifecycleDemo';

type Tab = 'hooks' | 'performance' | 'fetching' | 'debounce' | 'effects';

function App() {
  const [activeTab, setActiveTab] = useState<Tab>('hooks');

  const tabs: { id: Tab; label: string }[] = [
    { id: 'hooks', label: 'Hooks & State' },
    { id: 'performance', label: 'Performance' },
    { id: 'fetching', label: 'Data Fetching' },
    { id: 'debounce', label: 'Debounce/Throttle' },
    { id: 'effects', label: 'Effect Lifecycle' },
  ];

  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto py-6 px-4">
          <h1 className="text-3xl font-bold text-gray-900">
            React/Node Assessment Prep
          </h1>
          <p className="mt-1 text-gray-600">
            Interactive examples for all key concepts
          </p>
        </div>
      </header>

      <nav className="bg-white border-b">
        <div className="max-w-7xl mx-auto px-4">
          <div className="flex space-x-4">
            {tabs.map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`py-4 px-2 border-b-2 font-medium text-sm transition-colors ${
                  activeTab === tab.id
                    ? 'border-blue-500 text-blue-600'
                    : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                }`}
              >
                {tab.label}
              </button>
            ))}
          </div>
        </div>
      </nav>

      <main className="max-w-7xl mx-auto py-6 px-4">
        {activeTab === 'hooks' && <HooksDemo />}
        {activeTab === 'performance' && <PerformanceDemo />}
        {activeTab === 'fetching' && <DataFetchingDemo />}
        {activeTab === 'debounce' && <DebounceThrottleDemo />}
        {activeTab === 'effects' && <EffectLifecycleDemo />}
      </main>
    </div>
  );
}

export default App;
