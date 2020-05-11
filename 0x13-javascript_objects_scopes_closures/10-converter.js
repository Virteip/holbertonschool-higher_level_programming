#!/usr/bin/node

exports.converter = function (base) {
  return function (trans) {
    return trans.toString(base);
  };
};
