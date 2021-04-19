const mongoose = require('mongoose');

const Schema = mongoose.Schema;
const GameSchema = new Schema({
  name: String,
  players: [{
    type: Schema.Types.ObjectId,
    ref: 'Player',
  }],
  currentPlayer: {
    type: Schema.Types.ObjectId,
    ref: 'Player',
  },
  bigBlind: Number,
  smallBlind: Number,
  pot: Number,
  rounds: Number,
});
const GameModel = mongoose.model('Game', GameSchema);
module.exports = GameModel;
