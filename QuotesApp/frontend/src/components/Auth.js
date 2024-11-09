import React from 'react';
import { GoogleLogin } from 'react-google-login';
import api from '../api';

const Auth = ({ onLoginSuccess }) => {
  const handleSuccess = async (response) => {
    try {
      const res = await api.post('/auth/login', { token: response.tokenId });
      onLoginSuccess(res.data);
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  const handleFailure = (error) => {
    console.error('Google login error:', error);
  };

  return (
    <GoogleLogin
      clientId={process.env.REACT_APP_GOOGLE_CLIENT_ID}
      buttonText="Login with Google"
      onSuccess={handleSuccess}
      onFailure={handleFailure}
      cookiePolicy={'single_host_origin'}
    />
  );
};

export default Auth;