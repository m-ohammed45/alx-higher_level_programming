#!/usr/bin/node
const [,, arg1, arg2] = process.argv;

if (arg1 && arg2) {
  console.log(`${arg1} is ${arg2}`);
} else if (arg1 && !arg2) {
  console.log(`${arg1} is undefined`);
} else {
  console.log('undefined is undefined');
}
