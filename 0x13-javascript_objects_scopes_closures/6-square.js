#!/usr/bin/node
const SquareV2 = require('./5-square');

class Square extends SquareV2 {
  charPrint (c) {
    const character = c || 'X';

    for (let i = 1; i <= this.height; i++) {
      console.log(character.repeat(this.width));
    }
  }
}

module.exports = Square;
