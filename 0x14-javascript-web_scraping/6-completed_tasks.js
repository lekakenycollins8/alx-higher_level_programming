#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, { json: true }, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const tasksCompleted = {};
  body.forEach(todo => {
    if (todo.completed) {
      if (!tasksCompleted[todo.userId]) {
        tasksCompleted[todo.userId] = 1;
      } else {
        tasksCompleted[todo.userId] += 1;
      }
    }
  });
  console.log(tasksCompleted);
});
