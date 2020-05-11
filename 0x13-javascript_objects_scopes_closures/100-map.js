#!/usr/bin/node

const list = require('./100-data').list;

const newList = [];
let i = 0;

for (i; i < list.length; i++) {
  newList.push(list[i] * i);
}

console.log(list);
console.log(newList);
