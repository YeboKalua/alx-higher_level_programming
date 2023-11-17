#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      const empty = {};
      Object.setPrototypeOf(empty, Rectangle.prototype);
      return empty;
    }
  }
}

module.exports = Rectangle;
