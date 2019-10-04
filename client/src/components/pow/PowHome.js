import React, { Component } from 'react';
import axios from 'axios';
import PowTable from './PowTable'; 
import Container from 'react-bootstrap/Container';

export default class PowHome extends Component {
    constructor(props){
        super(props);
        this.state = {
            plans: null
        }
    }
    
    componentDidMount(){
        this.getPlans()
    }
    
    async getPlans() {
        const response = await axios.get('/api/plans');
        this.setState({
            plans: response.data
        })
    }
   
    render(){
        return(
           <Container> 
                <h1>Institutional Profile</h1>
                <PowTable plans={this.state.plans}/>
           </Container> 
        );
    }
}
