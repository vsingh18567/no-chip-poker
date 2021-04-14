const http = require("http");
const express = require("express");

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

io.on("connection", (socket) => {
  console.log("New client connected");
  if (interval) {
    clearInterval(interval);
  }
  interval = setInterval(() => getApiAndEmit(socket), 1000);
  socket.on("disconnect", () => {
    console.log("Client disconnected");
    clearInterval(interval);
  });
});

const getApiAndEmit = socket => {
  const response = new Date();
  // Emitting a new message. Will be consumed by the client
  socket.emit("FromAPI", response);
  console.log("message sent")
};

server.listen(port, () => console.log(`Listening on port ${port}`));