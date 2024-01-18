#!/usr/bin/node
const Squares = require('./5-squares');
class Square extends Squares {
    charPrint(c) {
        if (c === undefined) {
            c = 'X';
        }
        for (let i = 0; i < this.height; i++) {
          let row = '';
          for (let j = 0; j < this.width; j++) {
            row += 'c';
          }
          console.log(row);
        }
    }
}
module.exports = Square;