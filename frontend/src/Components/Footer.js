import React from 'react';
import "./landing.css";

export default function Footer() {
    return (
        <div >
            <footer style ={{
            fontSize: "14px",
            display: "flex",
            flexdirection: "row",
            alignItems: "center",
            width: "222%",
            /* border: 3px #270949 solid; */
            fontFamily: "Courier new",
            color:"whitesmoke",
            backgroundcolor: "#270949",
            float: "bottom",
            padding: "1% 10%",
            justifyItems: "center"
            }}>
            
                <div className = "contact">
                    Via Rossini 10, 10136 Turin Italy ||
                    +233 20 123 456  ||  
                    <a href = "mailto: rheeda.beecha@gmail.com" style = {{color: "white"}}>rheeda.beecha@gmail.com</a><br/>
                </div>

            </footer>
        </div>
    )
}
