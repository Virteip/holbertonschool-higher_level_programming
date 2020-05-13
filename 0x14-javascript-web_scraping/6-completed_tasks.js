#!/usr/bin/node

const request = require('request');
const nObj = {};

request(process.argv.slice(2)[0], function (error, body, response) {
  if (error) {
    console.log(error);
  } else {
    const contentJ = JSON.parse(response);

    try {
      for (const key of contentJ) {
        const id = key.userId;
        if (nObj[id] === undefined) { nObj[id] = 0; }
        if (key.completed === true) { nObj[id] += 1; }
      }
    } catch (error) {
    }
    console.log(nObj);
  }
});
