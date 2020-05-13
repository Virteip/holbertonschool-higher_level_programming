#!/usr/bin/node

const request = require('request');
const nObj = {};

request(process.argv.slice(2)[0], function (error, body, response) {
  if (body !== undefined) {
    const contentJ = JSON.parse(response);
    for (const key of contentJ) {
      const id = key.userId;
      if (nObj[id] === undefined) { nObxj[id] = 0; }
      if (key.completed === true) { nObj[id] += 1; }
    }
    console.log(nObj);
  } else {
    console.error(error);
  }
});
