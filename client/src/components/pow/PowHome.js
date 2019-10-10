import React, { Component } from 'react';
import axios from 'axios';
import PowTable from './PowTable'; 
import Container from 'react-bootstrap/Container';
import Jumbotron from 'react-bootstrap/Jumbotron';

export default class PowHome extends Component {
    constructor(props){
        super(props);
        this.state = {
            plans: []
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
                <Jumbotron>
                    <h1 className="text-center">Institutional Profile</h1>
                </Jumbotron>
                <h3>University of NIFA Combined Research and Extension</h3>
                <PowTable plans={this.state.plans}/>
           </Container> 
        );
    }
}
