#!/usr/bin/node
const { argv } = require('node:process');

if (argv === 0) {
  console.log('No argument');
} else if (argv === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
