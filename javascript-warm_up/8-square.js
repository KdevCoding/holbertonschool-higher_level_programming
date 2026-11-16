#!/usr/bin/node
const [first] = process.argv.slice(2);
const number = Number.parseInt(first, 10);

if (Number.isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    console.log('x'.repeat(number));
  }
}
