#!/usr/bin/node

// Print a square - nested loop
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  let x = 0;
  while (x < process.argv[2]) {
    console.log('X'.repeat(process.argv[2]));
    x++;
  }
}
