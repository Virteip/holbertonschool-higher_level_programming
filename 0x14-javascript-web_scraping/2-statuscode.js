#!/usr/bin/node

const request = require('request');

request(process.argv.slice(2)[0], function (error, response) {
  if (error != null) {
    console.error('error:', error);
  }
  console.log('code: ', response.statusCode);
});
