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

  rotate () {
    const wS = this.width;
    const hS = this.height;

    this.width = hS;
    this.height = wS;
  }

  double () {
    const wS = this.height;
    const hS = this.width;

    this.width = hS * 2;
    this.height = wS * 2;
  }

  print () {
    for (let i = 1; i <= this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
