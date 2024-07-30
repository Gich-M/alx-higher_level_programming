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
    console.error(`Error fetchimg URL ${url}:`, err);
    process.exit(1);
  }
    if (response.statusCode !== 200) {
        console.error(`Failed to fetch URL. Status code: ${response.statusCode}`);
        process.exit(1);
    }
      fs.writeFile(outpath, body, 'utf-8', (err) => {
        if (err) {
          console.error(`Error writing to file ${outpath}:`, err);
          process.exit(1);
        }
      });
});
