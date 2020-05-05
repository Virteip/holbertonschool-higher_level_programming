#!/usr/bin/node

if (process.argv[2]) {
  const myVar = process.argv.slice(2);
  console.log(myVar.join('\n'));
} else {
  console.log('No argument');
}
