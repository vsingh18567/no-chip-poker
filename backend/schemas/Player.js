const mongoose = require('mongoose');

const Schema = mongoose.Schema;
const PlayerSchema = new Schema({
  name: String,
  money: Number,
  bid: Number,
  isActive: Boolean,
  hasLeft: Boolean,
  playerNumber: Number,
});

const PlayerModel = mongoose.model('Player', PlayerSchema);


module.exports = PlayerModel;
