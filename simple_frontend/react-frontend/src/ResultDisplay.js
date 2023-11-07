import React from 'react';

function ResultDisplay({ predictions }) {
  return (
    <div className="ResultDisplay">
      <h2>API Prediction</h2>
      <pre>{JSON.stringify(predictions, null, 2)}</pre>
    </div>
  );
}

export default ResultDisplay;
