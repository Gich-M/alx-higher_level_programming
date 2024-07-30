#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

if (!url) {
  console.error('Usage: ./6-completed_tasks.js <url>');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status code:', response.statusCode);
    return;
  }

  const todos = JSON.parse(body);
  const completedTasksByUser = {};

  todos.forEach(task => {
    if (task.completed) {
      if (!completedTasksByUser[task.userId]) {
        completedTasksByUser[task.userId] = 0;
      }
      completedTasksByUser[task.userId]++;
    }
  });

  console.log(JSON.stringify(completedTasksByUser, null, 2));
});
