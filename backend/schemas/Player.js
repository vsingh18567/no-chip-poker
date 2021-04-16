var mongoose = require('mongoose');

var Schema = mongoose.Schema
var PlayerSchema = new Schema({
    name: String,
    money: Number,
    bid: Number,
    isActive: Boolean,
    hasLeft: Boolean,
    playerNumber: Number
})

var PlayerModel = mongoose.model("Player", PlayerSchema)


module.exports = PlayerModel;
