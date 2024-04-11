#!/usr/bin/node
const x = process.argv[2];

if (x) {
  const num = parseInt(x);
  if (!isNaN(num) && num > 0) {
    for (let i = 0; i < num; i++) {
      console.log("C is fun");
    }
}

}
