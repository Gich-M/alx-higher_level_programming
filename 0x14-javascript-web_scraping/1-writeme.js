#!/usr/bin/node

const fs = require('fs');
const filepath = process.argv[2];
const content = process.argv[3];

if (!filepath || !content) {
  console.error('Usage: ./1-writeme.js <filepath> <content>');
  process.exit(1);
}
fs.writeFile(filepath, content, 'utf-8', (err) => {
  if (err) {
    console.error('Error:', err);
    process.exit(1);
  }
});
