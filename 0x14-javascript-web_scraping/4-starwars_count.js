#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const characterId = '18';
let count = 0;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const films = JSON.parse(body).results;
  films.forEach(film => {
    film.characters.forEach((character) => {
      if (character.includes(characterId)) {
        count += 1;
      }
    });
  });
  console.log(count);
});
