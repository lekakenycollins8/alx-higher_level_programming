#!/usr/bin/node

function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);

  return (a + b);
}

const first_int = process.argv[2];
const second_int = process.argv[3];

if (first_int && second_int) {
  console.log(add(first_int, second_int));
} else {
  console.log(NaN);
}
