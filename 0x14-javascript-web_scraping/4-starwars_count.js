#!/usr/bin/node

const request = require('request');
let count = 0;

request(process.argv.slice(2)[0], function (error, body) {
  if (error) {
    console.error('error:', error);
  } else {
    for (const films of JSON.parse(body.body).results) {
      const charac = films.characters;
      for (const character of charac) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
