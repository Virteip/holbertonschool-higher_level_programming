#!/usr/bin/node

const request = require('request');
let films_json;

request('https://swapi-api.hbtn.io/api/films/', function (error, body) {
  if (error != null) {
    console.error('error:', error);
  }
  for (let i = 0; i < 6; i++ ) {
    films_json = JSON.parse(body.body).results[i].characters;
    console.log(i, films_json);
  }
});
