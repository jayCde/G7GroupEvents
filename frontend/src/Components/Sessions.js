import React from 'react';
import AfternoonSide from './AfternoonSide'
import EveningSide from './EveningSide'
import MorningSide from './MorningSide'
import './landing.css';
import {
    BrowserRouter as Router,
    Switch,
    Route,
  } from "react-router-dom";
//import "./index.css";
import EventListing from '../Pages1/EventListing';

export default function Sessions() {
    return (
        <Router>   
                <div className = "sessions">
                  <MorningSide/>
                  <AfternoonSide/>
                  <EveningSide/>
                </div>

            <Switch>
            <Route exact strict path="/eventlisting">
               <EventListing />
            </Route>
            </Switch>    
        </Router>         
    )
}
