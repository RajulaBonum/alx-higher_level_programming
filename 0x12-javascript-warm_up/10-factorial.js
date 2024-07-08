#!/usr/bin/node

// Write a script that computes and prints a factorial

function myFactorial (a) {
  if (isNaN(a)) {
    console.log(1);
  } else {
    let x = 1;
    let y = 1;

    while (x <= a) {
      y = y * x;
      x++;
    }
    console.log(y);
  }
}
myFactorial(parseInt(process.argv[2]));
