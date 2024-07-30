#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];

if (!movieID) {
  console.error('Usage: ./3-starwars_title.js <movieID>');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
    process.exit(1);
  }
  if (response.statusCode !== 200) {
    console.error('Movie not fetched. Status code: ${response.statusCode}');
    process.exit(1);
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
