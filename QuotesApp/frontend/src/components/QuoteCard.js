import React from 'react';

const QuoteCard = ({ quote }) => {
  return (
    <div className="quote-card">
      <p>{quote.content}</p>
      <small>Tags: {quote.tags.join(', ')}</small>
      <p>Rating: {quote.rating}</p>
    </div>
  );
};

export default QuoteCard;