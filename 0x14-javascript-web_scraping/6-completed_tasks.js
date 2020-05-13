#!/usr/bin/node

const request = require('request');
const nObj = {};

request(process.argv.slice(2)[0], function (error, response, body) {
  if (!error) {
    const contentJ = JSON.parse(body);
    if (contentJ.length !== undefined) {
      for (const key of contentJ) {
        const id = key.userId;
        if (nObj[id] === undefined) { nObj[id] = 0; }
        if (key.completed === true) { nObj[id]++; }
      }
    }
    console.log(nObj);
  }
});
