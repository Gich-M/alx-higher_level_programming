#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./101-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function fetchCharacter (url, callback) {
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error fetching character data:', error);
      callback(null);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('Failed to fetch character data. Status code:', response.statusCode);
      callback(null);
      return;
    }

    const character = JSON.parse(body);
    callback(character.name);
  });
}

request(movieUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch movie data. Status code:', response.statusCode);
    return;
  }

  const movie = JSON.parse(body);
  const characterUrls = movie.characters;

  characterUrls.forEach(url => {
    fetchCharacter(url, characterName => {
      if (characterName) {
        console.log(characterName);
      }
    });
  });
});
