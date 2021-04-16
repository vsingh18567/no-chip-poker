var mongoose = require('mongoose');

var Schema = mongoose.Schema
var GameSchema = new Schema({
    name: String,
    players: [{
        type: Schema.Types.ObjectId,
        ref: "Player"
    }],
    currentPlayer: {
        type: Schema.Types.ObjectId,
        ref: "Player"
    },
    bigBlind: Number,
    smallBlind: Number,
    pot: Number,
    rounds: Number,
})
var GameModel = mongoose.model('Game', GameSchema)
module.exports = GameModel;
