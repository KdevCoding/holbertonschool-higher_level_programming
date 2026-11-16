#!/usr/bin/node
const [first] = process.argv.slice(2);
const a = Number.parseInt(first, 10);
const [second] = process.argv.slice(3);
const b = Number.parseInt(second, 10);

function add (a, b) {
  return a + b;
}

console.log(add(a, b));
