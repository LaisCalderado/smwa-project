import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navigation from "./components/Navigation";
import Home from "./components/Home";
import Students from "./components/Students";
import Manage from "./components/Manage";
import Login from "./components/Login";
import Register from './components/Register';
import PrivateRoute from './components/PrivateRoute';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

function App() {

  const [authenticated, setAuthenticated] = useState(false);

  return (
    <BrowserRouter>
      <Navigation />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/manage" element={<Manage />} />
        <Route path="/students" element={<Students />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        {/* Rota protegida */}
        <Route
          path="/manage"
          element={
            <PrivateRoute
              element={<Manage />}
              isAuthenticated={authenticated}
              fallbackPath="/login"
            />
          }
        />
        <Route
          path="/students"
          element={
            <PrivateRoute
              element={<Students />}
              isAuthenticated={authenticated}
              fallbackPath="/login"
            />
          }
        />
        <Route
          path="/"
          element={
            <PrivateRoute
              element={<Home />}
              isAuthenticated={authenticated}
              fallbackPath="/login"
            />
          }
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;