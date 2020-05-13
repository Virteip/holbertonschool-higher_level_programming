#!/usr/bin/node

const fs = require('fs');

const request = require('request');

request(process.argv.slice(2)[0], function (error, body, response) {
  if (body !== undefined) {
    fs.writeFile(process.argv.slice(2)[1], response, 'utf-8', function (err) {
      if (err) {
        console.error(error);
      }
    });
  } else {
    console.error(error);
  }
});
