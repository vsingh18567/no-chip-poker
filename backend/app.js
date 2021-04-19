const http = require("http");
const express = require("express");
const message = require("../messages")
const app = express();
const server = http.createServer(app);

const io = require("socket.io")(server, {
    cors: {
        origin: "*",
        methods: ["GET", "POST"],
    }
});

const port = process.env.PORT || 3000;
const index = require("./routes/index");

app.use(index);

let interval;

io.on(message.PLAYER_CONNECT, (socket) => {
  console.log("New client connected");
  if (interval) {
    clearInterval(interval);
  }
  interval = setInterval(() => getApiAndEmit(socket), 1000);
  socket.on(message.PLAYER_DISCONNECT, () => {
    console.log("Client disconnected");
    clearInterval(interval);
  });

  socket.on(message.PLAYER_ADD, data => addPlayer(data));

  socket.on("Hi", () => {
    console.log("Hi");
  })
});

const getApiAndEmit = socket => {
  const response = new Date();
  // Emitting a new message. Will be consumed by the client
  socket.emit("FromAPI", response);
  console.log("message sent");
};

server.listen(port, () => console.log(`Listening on port ${port}`));