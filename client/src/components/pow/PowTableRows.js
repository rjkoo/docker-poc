import React from 'react';
import {Button, ButtonToolbar} from 'react-bootstrap'

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
                        <a href="#" role="button" className="btn btn-primary btn-sm">Edit</a>
                        <a href="#" role="button" className="btn btn-secondary btn-sm">Download</a>
                        </ButtonToolbar>
                    </td>
               </tr>
            </React.Fragment>
           ))
       }
       </tbody>
   ); 
};
