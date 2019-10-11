import React, { Component } from 'react';
import ContactPage from './ContactPage';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import config from './app.config';
import {Security, ImplicitCallback, SecureRoute } from '@okta/okta-react';

// Pages 
import PowHome from './components/pow/PowHome';
import PowEdit from './components/pow/edit/PowEdit';

function onAuthRequired({history}){
    history.push('/login');
}


class App extends Component
{
    state = {
        greeting: "Hi! - Greeting not set from API",
    };

    componentDidMount(){
        console.log('URL: ' + config.url);
        this.setGreeting();
    }

    async setGreeting(){
        const response = await axios.get('/api/hello');
        this.setState({greeting: response.data});
    }


    render (){
      return (
          <main> 
            <Route path='/' exact={true} component={PowHome} />
            <Route path='/contact' component={ContactPage} />
            <Route path='/edit/:id' component={PowEdit} />
          </main>
      );
    }
}
export default App;
