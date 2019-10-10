import React, { Component } from 'react';
import Table from 'react-bootstrap/Table';
import PowTableRows from './PowTableRows';
export default class PowTable extends Component {
    
    render(){
        return(
            <div className='pow-main'>
                <Table striped hover>
                    <thead>
                        <tr>
                            <th>Status</th>
                            <th>Year</th>
                            <th>Critical Issue Count</th>
                            <th></th>
                        </tr>
                    </thead>
                    <PowTableRows plans={this.props.plans}/>
                </Table>
            </div>
        );
    }
}

