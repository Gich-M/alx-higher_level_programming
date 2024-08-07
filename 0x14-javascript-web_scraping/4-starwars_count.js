#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterID = '18';

if (!url) {
  console.error('Usage: ./4-starwars_count.js <url>');
  process.exit(1);
}

request(url, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
    process.exit(1);
  }
  if (response.statusCode === 200) {
    const films = JSON.parse(body);

    const filmsWedgeAntilles = films.results.filter(film =>
      film.characters.some(character => character.endsWith(`/people/${characterID}/`))
    );
    console.log(filmsWedgeAntilles.length);
  } else {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
    process.exit(1);
  }
});
