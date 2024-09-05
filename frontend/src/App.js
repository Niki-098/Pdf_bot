import React from 'react';
import FileUpload from './components/FileUpload';
import QuestionForm from './components/QuestionForm';

function App() {
  return (
    <div>
      <h1>Chat with PDF</h1>
      <FileUpload />
      <QuestionForm />
    </div>
  );
}

export default App;
