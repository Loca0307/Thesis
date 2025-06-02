// create a web server

// import express
const express = require('express');
const app = express();

// import body-parser
const bodyParser = require('body-parser');
app.use(bodyParser.json());

// import comments.js
const comments = require('./comments');

// import cors
const cors = require('cors');
app.use(cors());

// get all comments
app.get('/comments', (req, res) => {
  const allComments = comments.getAllComments();
  res.json(allComments);
});

// post a new comment
app.post('/comments', (req, res) => {
  const newComment = req.body;
  comments.addComment(newComment);
  res.json(newComment);
});

// listen on port 3000
app.listen(3000, () => {
  console.log('Server is listening on port 3000');
});