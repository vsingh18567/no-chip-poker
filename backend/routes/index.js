const express = require("express");
const router = express.Router();
const Player = require("../schemas/Player")
const Game = require("../schemas/Game")
const mongoose = require('mongoose');
const mongoDB = "mongodb+srv://vsingh18567:$g!p5zF3KGW2Z4!@cluster0.jqcdc.mongodb.net/Cluster0?retryWrites=true&w=majority"
mongoose.connect(mongoDB, {useNewUrlParser: true, useUnifiedTopology: true})

var db = mongoose.connection;

db.on('error', console.error.bind(console, 'MongoDB connection error'));

router.get("/", (req, res) => {
  res.send({"info": "hit '/api' to get the RESTful endpoints, and hit '/ws' to get the websocket components"
})});

router.get("/games", (req, res) => {

  var iterateGames = (res) => {
    return function(err, data) {
      if (err) {
        console.log('err')
      }
      var response = []
      for (var game of data) {
        var gameData = {}
        gameData.name = game.name
        gameData.rounds = game.rounds,
        gameData.players = []
        for (var player of game.players) {
          gameData.players.push(player.name)
        }
        response.push(gameData)
      }
      res.send(response);
    }
  }
  Game.find({}, iterateGames(res));

})
router.post("/games", (req,res) => {

})

module.exports = router