#!/usr/bin/node
const fs = require('fs');
const filepath = process.argv[2];

if (!filepath) {
  console.error('Usage: ./0-readme.js <filepath>');
  process.exit(1);
}
fs.readFile(filepath, 'utf-8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
    process.exit(1);
  } else {
    console.log(data);
  }
});
