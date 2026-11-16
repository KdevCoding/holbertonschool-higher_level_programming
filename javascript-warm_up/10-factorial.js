#!/usr/bin/node
const [first] = process.argv.slice(2);
const number = Number.parseInt(first, 10);

function factorial (n) {
  if (Number.isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(number));
