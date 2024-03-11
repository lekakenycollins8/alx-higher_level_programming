#!/usr/bin/node

const int_value = parseInt(process.argv[2]);

if (!isNaN(int_value))
{
	console.log("My number:", int_value);
}
else
{
	console.log("Not a number");
}
