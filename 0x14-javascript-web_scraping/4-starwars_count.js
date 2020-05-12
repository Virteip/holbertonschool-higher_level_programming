#!/usr/bin/node

const request = require('request');
let filmsJson;
let count = 0;

request('https://swapi-api.hbtn.io/api/films/', function (error, body) {
  if (error) {
    console.error('error:', error);
  } else {
    for (let i = 0; i < 6; i++) {
      filmsJson = JSON.parse(body.body).results[i].characters;
      for (let i = 0; filmsJson[i] != null; i++) {
        if (filmsJson[i].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
