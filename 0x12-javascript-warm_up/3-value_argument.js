#!/usr/bin/node

// Script that prints the first argument
if (process.argv[2] !== undefined) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
