import React, { useState } from 'react';
import axios from 'axios';

function QuestionForm() {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async () => {
    const result = await axios.post('/ask/', { question });
    setResponse(result.data.answer);
  };

  return (
    <div>
      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />
      <button onClick={handleSubmit}>Ask</button>
      <div>{response}</div>
    </div>
  );
}

export default QuestionForm;
