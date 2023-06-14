#!/usr/bin/node
if (process.argv.length <= 2 || typeof parseInt(process.argv[2]) !== 'number') {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
