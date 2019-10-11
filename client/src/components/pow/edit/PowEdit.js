import React, { Component } from 'react';
import axios from 'axios';
import Container from 'react-bootstrap/Container';
import Jumbotron from 'react-bootstrap/Jumbotron';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
export default class PowEdit extends Component {
    constructor(props){
        super(props);
        this.state = {
            plan: {} // Initialize with an empty object
        }
    }
    
    componentDidMount(){
        console.log("Editing plan with id: " + this.props.match.params.id)
        // Query the Plan from API
        this.getPlan()
    }
    
    async getPlan(){
        const response = await axios.get('/api/plans/' + this.props.match.params.id);
        const plan = response.data
        this.setState({ plan });
    }
  

    render(){
        {console.log(this.state.plan.cohort)}
        {console.log(this.props.match.params)}
        return(
            <Container>
                <Jumbotron>
                    <h1 className="text-center">Edit Plan</h1>
                </Jumbotron>
                <h6>Cohort: {this.state.plan.cohort}</h6>
                <h6>Year: {this.state.plan.year}</h6>

                <Form>
                    <Form.Group controlId="summary">
                        <Form.Label><h5>Executive Summary</h5></Form.Label>
                        <Form.Control as="textarea" rows="5" value={this.state.plan.summary} />
                    </Form.Group>
                    
                    <Form.Group controlId="peer_review">
                        <Form.Label><h5>Merit/Peer Review</h5></Form.Label>
                        <Form.Control as="textarea" rows="5" value={this.state.plan.merit_peer_review} />
                    </Form.Group>
                   
                    <fieldset>
                        <Form.Group controlId="peer_review">
                            <Form.Label><h5>Stakeholder Input: Actions to Seek</h5></Form.Label>
                            <Form.Control as="textarea" rows="5" value={this.state.plan.stakeholder_actions} />
                        </Form.Group>

                        <Form.Group controlId="peer_review">
                            <Form.Label><h5>Stakeholder Input: Methods to Identify</h5></Form.Label>
                            <Form.Control as="textarea" rows="5" value={this.state.plan.stakeholder_id_methods} />
                        </Form.Group>
                        
                    </fieldset>

                    <Button variant="primary" type="submit">
                        Submit
                     </Button>
                </Form>

           </Container> 
        );
    }
}
