import React, { useEffect, useState } from 'react';
import api from '../api';
import QuoteCard from '../components/QuoteCard';

const Profile = () => {
  const [userQuotes, setUserQuotes] = useState([]);

  useEffect(() => {
    const fetchUserQuotes = async () => {
      try {
        const response = await api.get('/user/quotes');
        setUserQuotes(response.data);
      } catch (error) {
        console.error('Error fetching user quotes:', error);
      }
    };
    fetchUserQuotes();
  }, []);

  return (
    <div>
      <h1>Your Quotes</h1>
      {userQuotes.map((quote) => (
        <QuoteCard key={quote.id} quote={quote} />
      ))}
    </div>
  );
};

export default Profile;