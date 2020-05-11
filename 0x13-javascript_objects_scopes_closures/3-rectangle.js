#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w <= 0 || !Number.isInteger(w)) || (h <= 0 || !Number.isInteger(h))) {
      this.width = undefined;
      this.height = undefined;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 1; i <= this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
