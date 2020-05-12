#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv.slice(2)[0], function (error, body) {
  if (error === null) {
    console.error('error:', error);
  }else{
    console.log(JSON.parse(body.body).title);
  }
});
