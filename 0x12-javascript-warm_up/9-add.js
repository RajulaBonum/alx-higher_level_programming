#!/usr/bin/node

// Write a script that prints the addition of 2 integers
function add (a, b) {
  const result = a + b;
  console.log(result);
}
add(parseInt(process.argv[2]), parseInt(process.argv[3]));
