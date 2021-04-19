import React, {useState, useEffect} from 'react';
import {useRouter} from 'next/router';
import Button from 'react-bootstrap/Button'
import socketIOClient from "socket.io-client";
const ENDPOINT = "http://localhost:3000/"


function App() {
    const [response, setResponse] = useState("");
    const router = useRouter();
    const { game } = router.query;

  useEffect(() => {
    const socket = socketIOClient(ENDPOINT);
    socket.on("FromAPI", data => {
      setResponse(data);
    })
  }, []);

  const sendSignal = () => {
    console.log("hi");
    const socket = socketIOClient(ENDPOINT);
    socket.emit("Hi")
  }
  return (
    <div>
    <p>
      {game} It's <time dateTime={response}>{response}</time>
    </p>
    <Button onClick={sendSignal}>Hi</Button>
    </div>

  );
}

export default App;
  
