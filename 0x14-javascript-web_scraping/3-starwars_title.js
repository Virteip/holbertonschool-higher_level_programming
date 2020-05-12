#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv.slice(2)[0], function (error, body) {
  if (JSON.parse(body.body).title !== undefined) {
    console.log(JSON.parse(body.body).title);
  }
  if (error) {
    console.error(error);
  }
});
