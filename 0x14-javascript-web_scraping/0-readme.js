#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv.slice(2)[0], function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
