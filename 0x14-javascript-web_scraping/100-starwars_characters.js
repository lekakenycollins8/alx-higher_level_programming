#!/usr/bin/node

const request = require('request');
const title = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${title}`;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    request(character, (err, response, body) => {
      if (err) {
        console.error(err);
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  }
});
