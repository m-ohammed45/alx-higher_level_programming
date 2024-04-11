#!/usr/bin/env node

const arg = process.argv[2];

const numOccurrences = parseInt(arg, 10);
let occurrences = numOccurrences;

if (isNaN(occurrences)) {
  console.log('Missing number of occurrences');
} else {
 
  while (occurrences > 0) {
    console.log('C is fun');
    occurrences--;
  }
}
