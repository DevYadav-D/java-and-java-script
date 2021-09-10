import React from 'react';
import './App.css';
import { TodoPage } from './Pages/TodoPage'
import {Show} from './Pages/Show'

import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";

// import {useState, useEffect} from 'react';

function App() {

  // const [articles, setArticles] = useState([])

  // useEffect(() => {
  //   fetch('http://127.0.0.1:5000/get', {
  //     'methods':'GET',
  //     headers: {
  //       'Content-Type':'applications/json'
  //     }
  //   })
  //   .then(resp => resp.json())
  //   .then(resp => setArticles(resp))
  //   .catch(error => console.log(error))
  // },[])
  return (
    
    <div className="App">
      {/* <TodoPage/> 
      flask and react js course */}
      
      <Router>
      <Switch>
        <Route exact path='/'>
          <TodoPage/>
        </Route>
        <Route path='/:id'>
          <Show/>
        </Route>
      </Switch>
    </Router>
      
    </div>
  );
}

export default App;
