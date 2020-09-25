import React from 'react'
import Speaker from '../Components/Speaker'
import EventDetails from '../Components/EventDetails';
import "../Components/index.css";

export default function Event() {
    return (
        <div className = "event">
           
            <div className = "details"> 
            <Speaker/>
            <EventDetails/>
            </div>
            
        </div>
    )
}
