#!/usr/bin/node

const request = require('request');

// Function to retrieve character names in the exact order
const getCharacterNames = (filmId) => {
    const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

    // Making a request to get film details
    request(url, (err, res, body) => {
        if (err) {
            console.error(err);
            return;
        }

        // Parsing film details
        const filmData = JSON.parse(body);
        const characters = filmData.characters;

        // Displaying character names in the exact order
        characters.forEach((characterUrl) => {
            request(characterUrl, (err, res, body) => {
                if (err) {
                    console.error(err);
                    return;
                }

                const characterData = JSON.parse(body);
                console.log(characterData.name);
            });
        });
    });
};

// Handling command line argument
const filmId = process.argv[2];
if (!filmId) {
    console.error('Please provide a film ID as a command line argument.');
    process.exit(1);
}

// Calling the function to retrieve and display character names
getCharacterNames(filmId);
