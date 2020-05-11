#!/usr/bin/node

let obj = 0;
exports.logMe = function (item) {
  console.log(obj + ': ' + item);
  obj++;
  return obj;
};
