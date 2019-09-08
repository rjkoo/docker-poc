import React, { Component } from 'react';
import ContactPage from './ContactPage';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';
class App extends Component
{
    state = {
        greeting: "Hi! - Greeting not set from API"
    };

    componentDidMount(){
        this.setGreeting();
    }

    async setGreeting(){
        const response = await axios.get('/api/hello');
        this.setState({greeting: response.data});
    }

    render (){
      return (
        <Router>
            <div className="App">
              <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <a
                  className="App-link"
                  href="https://reactjs.org"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                { this.state.greeting}
                </a>
                <Link to='/contactpage'>Contact Form</Link>
              </header>
                <div>
                    <Route exact path="/contactpage" component={ContactPage} />
                    
                </div>
            </div>
        </Router>
      );
    }
}

/*
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Hello, World!!
        </a>
      </header>
    </div>
  );
}
*/
export default App;
