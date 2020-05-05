#!/usr/bin/node
const intRegex = /^\d+$/;

if (intRegex.test(process.argv[2])) {
  console.log('My number: ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
