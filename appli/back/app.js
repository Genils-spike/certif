const express = require('express');
const mongoose = require('mongoose');
const morgan = require('morgan');
const bodyParser = require('body-parser');

//Port definition
const port = process.env.PORT || 3030;

const app = express()

//Logger
app.use(morgan('dev'));
app.use(bodyParser.urlencoded({extended : true}));
app.use(bodyParser.json());

//Database connection
mongoose.Promise = global.Promise
mongoose.connect('mongodb://localhost/renzen')

app.use('/users', require('.'))

app.listen(port);

console.log("Server is OKAY")
