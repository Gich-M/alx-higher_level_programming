#!/usr/bin/node

const integers = process.argv.slice(2).map(Number);

const sorted  = integers.sort((a, b) => b - a);

if (sorted.length < 2)
{
	console.log(0);
}
else
{
	console.log(sorted[1]);
}
