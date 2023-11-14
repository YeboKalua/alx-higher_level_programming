#!/usr/bin/node
function sort (arr) {
  const len = arr.length;
  for (let i = 0; i < len - 1; i++) {
    for (let j = 0; j < len - 1 - i; j++) {
      if (arr[j] > arr[j + 1]) {
        const temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
  return arr;
}
const array = process.argv.slice(2).map(Number);
const newArray = sort(array);
const num = newArray.length;
if (num < 2) {
  console.log(0);
} else {
  console.log(newArray[num - 2]);
}
