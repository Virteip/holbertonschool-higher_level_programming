#!/usr/bin/node

const fs = require('fs');

try {
  const data = fs.readFileSync(process.argv.slice(2)[0], 'utf8');
  console.log(data);
} catch (err) {
  console.error(err);
}
