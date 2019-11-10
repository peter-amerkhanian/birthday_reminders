import React, {useEffect, useState} from 'react';
import './App.css';
import {Names} from "./components/Names";

function App() {
    const [names, setNames] = useState([]);
    useEffect(() => {
        fetch('http://localhost:5000/all_calendar_names').then(response =>
            response.json().then(data => {
                setNames(data.names)
            })
        )
    }, []);
    console.log(names);
    return (
        <div className="App">
        <Names names={names} />
        </div>
    );
}

export default App;
