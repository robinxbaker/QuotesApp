import React, { useState } from 'react';
import api from '../api';

const QuoteForm = ({ onQuoteAdded }) => {
  const [content, setContent] = useState('');
  const [tags, setTags] = useState('');
  const [isPublic, setIsPublic] = useState(true);
  const [isAnonymous, setIsAnonymous] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await api.post('/api/quotes', {
        content,
        tags,
        is_public: isPublic,
        is_anonymous: isAnonymous
      });
      if (response.status === 201) {
        onQuoteAdded();
        setContent('');
        setTags('');
      }
    } catch (error) {
      console.error('Error creating quote:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <textarea
        value={content}
        onChange={(e) => setContent(e.target.value)}
        placeholder="Write your quote..."
        required
      />
      <input
        type="text"
        value={tags}
        onChange={(e) => setTags(e.target.value)}
        placeholder="Tags (comma-separated)"
      />
      <label>
        <input type="checkbox" checked={isAnonymous} onChange={() => setIsAnonymous(!isAnonymous)} />
        Post Anonymously
      </label>
      <label>
        <input type="checkbox" checked={isPublic} onChange={() => setIsPublic(!isPublic)} />
        Make Public
      </label>
      <button type="submit">Add Quote</button>
    </form>
  );
};

export default QuoteForm;