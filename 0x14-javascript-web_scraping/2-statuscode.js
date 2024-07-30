#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

if (!url) {
  console.error('Usage: ./2-statuscode.js <url>');
  process.exit(1);
}

request.get(url, (err, response) => {
  if (err) {
    console.error('Error:', err);
    process.exit(1);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
