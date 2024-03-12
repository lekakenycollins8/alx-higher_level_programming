#!/usr/bin/node

const integers = process.argv.slice(2).map(Number);

integers.sort((a, b) => b - a);

if (integers.length === 0 || integers.length === 1) {
  console.log(0);
} else {
  console.log(integers[1]);
}
