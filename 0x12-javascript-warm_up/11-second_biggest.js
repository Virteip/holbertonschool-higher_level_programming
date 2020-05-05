#!/usr/bin/node
const intArray = process.argv.splice(2);
const arrLength = process.argv.length;
let result;

function secondLargest (intArray) {
  result = intArray.reverse().filter(num => num >= 0);
  return result[1];
}

if (arrLength > 1) {
  console.log(secondLargest(intArray));
} else {
  console.log(0);
}
