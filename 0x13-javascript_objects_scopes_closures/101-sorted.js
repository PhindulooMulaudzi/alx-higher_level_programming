#!/usr/bin/node
const dict = require ('./101-data').dict;

const newDict = new Map ();

Object.entries (dict).forEach (([key, value]) => {
  if (!newDict.has (value)) {
    newDict.set (value, []);
  }
  newDict.get (value).unshift (key);
});

console.log (Object.fromEntries (newDict));
