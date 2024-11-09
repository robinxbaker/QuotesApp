import React from 'react';
import Auth from '../components/Auth';

const Login = ({ onLoginSuccess }) => {
  return (
    <div className="login-page">
      <h2>Welcome to Quotes App</h2>
      <Auth onLoginSuccess={onLoginSuccess} />
    </div>
  );
};

export default Login;