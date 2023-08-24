import React from 'react';
import { Navigate, Route } from 'react-router-dom';

const PrivateRoute = ({ element: Element, isAuthenticated, fallbackPath, ...rest }) => {
  return isAuthenticated ? <Element {...rest} /> : <Navigate to={fallbackPath} />;
};

export default PrivateRoute;
