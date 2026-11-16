#!/usr/bin/node
const { argv } = require('node:process');
let first = 0;
let second = 0;
if (argv.length < 5) {
  console.log(0);
} else {
  argv.forEach((val) => {
    if (val > first) {
      second = first;
      first = val;
    }
  });
  console.log(second);
}
