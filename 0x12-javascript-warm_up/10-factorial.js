#!/usr/bin/node
function factorial (n) {
  if (n === 1) {
    return (1);
  } else if (isNaN(n)) {
    return (NaN);
  }
  return (n * factorial(n - 1));
}

console.log(factorial(process.argv[2]));
