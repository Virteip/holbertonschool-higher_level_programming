#!/usr/bin/node

if (process.argv[2]) {
  const myVar = process.argv.slice(2);
  console.log(myVar.join(' '));
} else {
  console.log('No argument');
}
