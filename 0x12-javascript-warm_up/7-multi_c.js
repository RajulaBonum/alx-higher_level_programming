#!/usr/bin/node

// Print multiple times
if (isNaN(process.argv[2]) || process.argv === undefined) {
  console.log('Missing number of occurrences');
} else {
  let x = 0;
  while (x < parseInt(process.argv[2])) {
    console.log('C is fun');
    x++;
  }
}
