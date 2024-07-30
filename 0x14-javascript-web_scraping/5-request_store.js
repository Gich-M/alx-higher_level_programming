#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const outpath = process.argv[3];

if (!url || !outpath) {
  console.error('Usage: ./5-request_store.js <url> <outpath>');
  process.exit(1);
}

request.get(url, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
    process.exit(1);
  } else {
    if (response.statusCode === 200) {
      fs.writeFile(outpath, body, 'utf-8', (err) => {
        if (err) {
          console.error('Error writing to file:', err);
          process.exit(1);
        } else {
          console.log(`${outpath}`);
        }
      });
    } else {
      console.error(`Failed to fetch URL. Status code: ${response.statusCode}`);
      process.exit(1);
    }
  }
});
