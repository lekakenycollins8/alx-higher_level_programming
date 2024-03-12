#!/usr/bin/node

function factorial (N) {
  if (N === NaN || N === 1) {
    return 1;
  }
  return N * factorial(N - 1);
}

const first_arg = process.argv[2];

if (first_arg) {
  console.log(factorial(first_arg));
} else {
  console.log(1);
}
