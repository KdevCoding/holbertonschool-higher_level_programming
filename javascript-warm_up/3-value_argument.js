const [first] = process.argv.slice(2);

if (first === undefined) {
  console.log('No argument');
} else {
  console.log(first);
}
