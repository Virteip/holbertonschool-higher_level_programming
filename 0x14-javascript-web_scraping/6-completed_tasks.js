#!/usr/bin/node

const request = require('request');
const nObj = {};

request(process.argv.slice(2)[0], function (error, response, body) {
  if (!error) {
    const jContent = JSON.parse(body);
    for (const key of jContent) {
      if (key.completed === true) {
        if (nObj[key.userId] === undefined) { nObj[key.userId] = 0; }
        nObj[key.userId] += 1;
      }
    }
    console.log(nObj);
  }
});
