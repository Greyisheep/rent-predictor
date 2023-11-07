import React, { useState } from 'react';
import './App.css';
import InputForm from './InputForm';
import ResultDisplay from './ResultDisplay';

function App() {
  const [predictions, setPrediction] = useState(null);

  const updateResult = (data) => {
    setPrediction(data);
  };

  return (
    <div className="App">
      <h1>FastAPI React Frontend</h1>
      <InputForm updateResult={updateResult} />
      {predictions && <ResultDisplay predictions={predictions} />}
    </div>
  );
}

export default App;
