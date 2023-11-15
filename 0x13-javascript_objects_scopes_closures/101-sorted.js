#!/usr/bin/node
const dict = require ('./101-data').dict;

const newDict = Object.fromEntries (
  [...new Set (Object.values (dict))].map (value => [
    value,
    Object.entries (dict)
      .filter (([key, dictValue]) => dictValue === value)
      .map (([key]) => key),
  ])
);

console.log (newDict);
