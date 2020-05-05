#!/usr/bin/node

if (process.argv.length < 3) {
  console.log('No argument');
} else {
  const myVar = process.argv.slice(2);

  console.log(myVar.join('\n'));
}
