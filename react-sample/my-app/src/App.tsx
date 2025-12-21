import React from 'react';
import logo from './logo.svg';
import './App.css';
import Greeting from './Greeting';
import Counter from './Counter';

function App() {
  // return (
  //   <div className="App">
  //     <header className="App-header">
  //       <img src={logo} className="App-logo" alt="logo" />
  //       <p>
  //         Edit <code>src/App.tsx</code> and save to reload.
  //       </p>
  //       <a
  //         className="App-link"
  //         href="https://reactjs.org"
  //         target="_blank"
  //         rel="noopener noreferrer"
  //       >
  //         William Learns React
  //       </a>
  //     </header>
  //   </div>
  // );
  return (
    <>
      <Greeting name="Alice" />
      <Greeting name="Bob" />
      <Counter></Counter>
    </>
  )
}

export default App;
