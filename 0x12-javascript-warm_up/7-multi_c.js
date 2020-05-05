#!/usr/bin/node
let i;
let intRegex = /^\d+$/;
const myInt = process.argv[2];

if (intRegex.test(parseInt(process.argv[2]))) {
  for (i = 0; i <= (process.argv[2] - 1); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
