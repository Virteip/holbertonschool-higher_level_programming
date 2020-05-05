#!/usr/bin/node
let i;
const myInt = process.argv[2];

if (parseInt(process.argv[2]) == myInt) {
  for (i = 0; i <= (process.argv[2] - 1); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
