#!/usr/bin/node
const [first] = process.argv.slice(2);

const number = Number.parseInt(first, 10);

if (Number.isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
