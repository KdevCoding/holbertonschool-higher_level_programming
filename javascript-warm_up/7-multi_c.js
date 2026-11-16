#!/usr/bin/node
const [first] = process.argv.slice(2);
const text = 'C is fun';
const number = Number.parseInt(first, 10);

if (Number.isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < number; i++) {
    console.log(text);
  }
}
