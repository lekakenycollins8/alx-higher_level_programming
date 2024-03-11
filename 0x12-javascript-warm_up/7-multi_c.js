#!/usr/bin/node

const x_tms = parseInt(process.argv[2]);

if (!isNaN(x_tms))
{
	for (let i = 0; i < x_tms; i++)
	{
		console.log("C is fun");
	}
}
else
{
	console.log("Missing number of occurrences");
}
