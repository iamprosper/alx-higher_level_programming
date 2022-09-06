#!/usr/bin/node
/*
if (typeof(+ process.argv[3]) === NaN){
    console.log('Not a number');
}
else if (typeof(+ process.argv[3] === Number)){
    console.log(`My number: $process.argv[3]`);
}
if (typeof(process.argv[2]) == undefined){
  console.log('Not a number');
}
*/
if (!parseInt(process.argv[2])) console.log('Not a number');
else if (String(parseInt(process.argv[2])).split('').length === process.argv[2].split('').length) console.log(`My number ${process.argv[2]}`);
else console.log('Not a number');
/*
if (parseInt(process.argv[2]) === NaN) console.log('Not a number');
else console.log(`My number ${process.argv[2]}`);
*/
