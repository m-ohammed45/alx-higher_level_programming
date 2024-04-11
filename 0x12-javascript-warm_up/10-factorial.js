#!/usr/bin/node

function fact (a) {
  if ((isNaN(a)) || (a === 1)) {
    return 1;
  } else {
    return a * fact(a - 1);
  }
}
console.log(fact(parseInt(process.argv[2])));
