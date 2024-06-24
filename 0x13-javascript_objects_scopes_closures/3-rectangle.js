#!/usr/bin/node
/**
 * Represents parallelogram with 4 right angles.
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let x = '';
      for (let l = 0; l < this.width; l++) {
        x += 'X';
      }
      console.log(x);
    }
  }
}

module.exports = Rectangle;
