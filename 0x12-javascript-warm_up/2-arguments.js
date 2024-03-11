#!/usr/bin/node

const argvLength = process.argv.length - 1;

if (argvLength === 1)
{
	console.log("No argument");
}
else if (argvLength === 2)
{
	console.log("Argument found");
}
else
{
	console.log("Arguments found");
}
