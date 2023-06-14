#!/usr/bin/node
let x = '';
if (isNaN(parseInt(process.argv[2])) || process.argv.length <= 2) {
  console.log('Missing size');
} else {
  for (let width = 0; width < process.argv[2]; width++) {
    for (let length = 0; length < process.argv[2]; length++) {
      x = x.concat('X');
    }
    console.log(x);
    x = '';
  }
}
