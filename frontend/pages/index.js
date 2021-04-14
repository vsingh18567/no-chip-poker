
import React, {useState, useEffect} from 'react';
import socketIOClient from "socket.io-client";
const ENDPOINT = "http://localhost:3000/"

class AppC extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      response: ""
    }
    this.socket = socketIOClient(ENDPOINT);

  }

  componentDidMount() {

    this.socket.on("FromAPI", data => {
      this.setState({response: data});
    })
  }

  componentDidUpdate() {
    this.socket.on("FromAPI", data => {
      this.setState({response: data});
    })
  }

  render () {
    return (
      <p>
        It's <time dateTime={this.state.response}>{this.state.response}</time>
      </p>
    );
  }
}

function App() {
  const [response, setResponse] = useState("");

  useEffect(() => {
    const socket = socketIOClient(ENDPOINT);
    socket.on("FromAPI", data => {
      setResponse(data);
    })
  }, []);

  return (
    <p>
      It's <time dateTime={response}>{response}</time>
    </p>
  );
}

export default App;
  
