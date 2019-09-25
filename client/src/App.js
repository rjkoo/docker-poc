import React, { Component } from 'react';
import ContactPage from './ContactPage';
import Profile from './Profile';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

import {Security, ImplicitCallback, SecureRoute } from '@okta/okta-react';
import Home from './Home';
import Login from './Login';
import Protected from './Protected';
import RegistrationForm from './RegistrationForm';

import config from './app.config';

function onAuthRequired({history}){
    history.push('/login');
}


class App extends Component
{
    state = {
        greeting: "Hi! - Greeting not set from API"
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
        <Router>
            <Security
                issuer={config.url}
                clientId={config.clientId}
                redirectUri={config.redirectUri}
                onAuthRequired={onAuthRequired}
                pkce={true}>
            
                <Route path='/' exact={true} component={Home} />
                <SecureRoute path='/protected' component={Protected} />
                <SecureRoute path='/profile' component={Profile} />
                <Route path='/login' render={() => <Login baseUrl='https://dev-956783.okta.com'/>} />
                <Route path='/implicit/callback' component={ImplicitCallback} />
                <Route path='/register' component={RegistrationForm} />
                <Route path='/contact' component={ContactPage} />
            </Security>
        </Router>
      );
    }
}
export default App;
