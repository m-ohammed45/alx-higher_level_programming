#!/usr/bin/node
const x = process.argv[2];

if (!isNaN(x) && parseInt(x) > 0) {
  for (let i = 0; i < parseInt(x); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
