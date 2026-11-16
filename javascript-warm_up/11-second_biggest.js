#!/usr/bin/node
const { argv } = require('node:process');
let first = 0;
let second = 0;
if (argv.length < 4) {
  console.log(0);
} else {
  argv.forEach((val) => {
    console.log(val);
    if (Number(val) > first) {
      second = first;
      first = val;
    } else if (Number(val) > second) {
      second = val;
    }
  });
  console.log(second);
}
