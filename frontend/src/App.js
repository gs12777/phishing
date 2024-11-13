import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [url, setUrl] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null); // Clear previous errors

    try {
      const response = await axios.post('http://localhost:5000/api/check', { url });
      setResult(response.data);  // Successful response
    } catch (err) {
      if (err.response) {
        // Backend responded with an error status
        console.error('Backend Error:', err.response.data); // Log the error response
        setError(err.response.data.message || 'An error occurred. Please try again.');
      } else {
        // Error due to network issue or other problems
        console.error('Error:', err);  // Log the error details
        setError('An error occurred while checking the URL. Please try again.');
      }
    }
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

      {error && (
        <div className="error-message">
          <p>{error}</p>
        </div>
      )}

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
