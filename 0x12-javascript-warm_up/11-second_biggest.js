#!/usr/bin/node

// Write a script that searches the second biggest integer in the list of arguments.

if (process.argv.length <= 3) {
	console.log('0');
} else {
	const myArr = process.argv.slice(2).map(Number);
	const second = arr.sort(function (a, b) { return b - a;})[1];
	console.log(second);
}
