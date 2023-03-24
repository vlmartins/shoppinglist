import { Routes, Route } from 'react-router-dom';
import React, {useEffect} from 'react'
import Test from './test.jsx'
import Login from  './components/Login.jsx'
import Layout from './components/Layout';
import SignUp from './components/SignUp';
import ShoppingList from './components/shoppinglist/ShoppingList';



function App() {
  return (
    <div >
    <Routes>
        <Route path="/" element={<Layout />}>
        </Route>
         <Route path="/login" element={<Login />} />
         <Route path="/signup" element={<SignUp />} /> 
         <Route path="/shoppinglist" element={<ShoppingList />} /> 
    </Routes>    
    </div>
  )
}

export default App
