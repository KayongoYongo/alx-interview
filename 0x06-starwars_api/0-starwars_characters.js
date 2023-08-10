#!/usr/bin/node

const request = require('request');

function getMovieCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error("Error fetching movie data:", error.message);
        reject([]);
      } else if (response.statusCode === 200) {
        const filmData = JSON.parse(body);
        const characterUrls = filmData.characters;
        const characterPromises = characterUrls.map(charUrl => {
          return new Promise((resolveChar, rejectChar) => {
            request(charUrl, (charError, charResponse, charBody) => {
              if (charError) {
                rejectChar(charError);
              } else {
                const charData = JSON.parse(charBody);
                resolveChar(charData.name);
              }
            });
          });
        });

        Promise.all(characterPromises)
          .then(characterNames => {
            resolve(characterNames);
          })
          .catch(err => {
            console.error("Error fetching character data:", err.message);
            resolve([]);
          });
      } else {
        console.error("Error fetching movie data. Status code:", response.statusCode);
        reject([]);
      }
    });
  });
}

if (process.argv.length < 3) {
  console.log("Usage: node script_name.js movie_id");
  process.exit(1);
}

const movieId = process.argv[2];
getMovieCharacters(movieId)
  .then(characterNames => {
    characterNames.forEach(name => {
      console.log(name);
    });
  });
