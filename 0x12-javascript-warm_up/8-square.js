#!/usr/bin/node
let i = 0;
let j = 0;
const num = parseInt(process.argv[2]);
if (!isNaN(num)) {
  for (i = 0; i < num; i++) {
    let row = '';
    for (j = 0; j < num; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
