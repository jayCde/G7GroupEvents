import React from 'react';
import NavBar from "../Components/NavBar";
import Footer from "../Components/Footer";
import Sessions from '../Components/Sessions';

export default function LandingPage() {
    return (
        <div>
            <NavBar/>
            <Sessions/>
            <Footer/>
        </div>
    )
}
