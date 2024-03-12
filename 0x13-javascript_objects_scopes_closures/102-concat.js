#!/usr/bin/node

const fs = require('fs');

const firstArg = process.argv[2];
const secondArg = process.argv[3];
const thirdArg = process.argv[4];

const firstArgContent = fs.readFileSync(firstArg, 'utf8');

const secondArgContent = fs.readFileSync(secondArg, 'utf8');

const thirdArgContent = firstArgContent + secondArgContent;

fs.writeFileSync(thirdArg, thirdArgContent, 'utf8');
