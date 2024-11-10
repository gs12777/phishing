import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [url, setUrl] = useState('');
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.post('http://localhost:5000/api/check', { url });
    setResult(response.data);
  };

  return (
    <div className="App">
      <h1>Phishing URL Detector</h1>
      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          value={url} 
          onChange={(e) => setUrl(e.target.value)} 
          placeholder="Enter URL to check" 
          required 
        />
        <button type="submit">Check URL</button>
      </form>
      {result && (
        <div>
          <h2>Result:</h2>
          <p>{result.message}</p>
        </div>
      )}
    </div>
  );
}

export default App;
