import React from 'react';
import {Button, ButtonToolbar} from 'react-bootstrap';
import {Link} from 'react-router-dom';

export default ({plans}) => {
        console.log(plans.length)
   return (
       <tbody>
       {
           plans.map( p => (
            <React.Fragment key={p.id}>
               <tr>
                    <td>{p.status}</td>
                    <td>{p.year}</td>
                    <td>{p.number_of_critical_issues}</td>
                    <td>
                        <ButtonToolbar className="d-flex justify-content-end">
                            <Link to={'/edit/'+ p.id} role="button" className="btn btn-primary btn-sm">Edit</Link>
                            <a href="http://www.africau.edu/images/default/sample.pdf" role="button" className="btn btn-secondary btn-sm">Download</a>
                        </ButtonToolbar>
                    </td>
               </tr>
            </React.Fragment>
           ))
       }
       </tbody>
   ); 
};
