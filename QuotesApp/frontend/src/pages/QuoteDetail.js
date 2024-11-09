import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import api from '../api';

const QuoteDetail = () => {
  const { id } = useParams();
  const [quote, setQuote] = useState(null);

  useEffect(() => {
    const fetchQuote = async () => {
      try {
        const response = await api.get(`/api/quotes/${id}`);
        setQuote(response.data);
      } catch (error) {
        console.error('Error fetching quote:', error);
      }
    };
    fetchQuote();
  }, [id]);

  if (!quote) return <p>Loading...</p>;

  return (
    <div>
      <h2>{quote.content}</h2>
      <p>Tags: {quote.tags}</p>
      <p>Rating: {quote.rating}</p>
    </div>
  );
};

export default QuoteDetail;