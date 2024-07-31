#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./script.js <Movie ID>');
  process.exit(1);
}

const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function fetchCharacter (url, callback) {
  request(url, (error, response, body) => {
    if (error || response.statusCode !== 200) {
      callback(null);
      return;
    }
    const character = JSON.parse(body);
    callback(character.name);
  });
}

request(movieUrl, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error('Failed to fetch movie data.');
    return;
  }

  const movie = JSON.parse(body);
  const characterUrls = movie.characters;

  function fetchCharactersSequentially (index) {
    if (index >= characterUrls.length) return;

    fetchCharacter(characterUrls[index], (characterName) => {
      if (characterName) {
        console.log(characterName);
      }
      fetchCharactersSequentially(index + 1);
    });
  }

  fetchCharactersSequentially(0);
});
