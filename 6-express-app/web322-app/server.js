/*********************************************************************************
* WEB322 – Assignment 02
* I declare that this assignment is my own work in accordance with Seneca Academic Policy. No part
* of this assignment has been copied manually or electronically from any other source
* (including 3rd party web sites) or distributed to other students.
*
* Name: Jungwook Kweon  Student ID: ______________ Date: ________________
*
* Online (Heroku) Link: ________________________________________________________
*
********************************************************************************/ 
// Importing modules
var express = require('express');
var dataService = require('./data_service');
const path = require("path");

// Initialize express app
var app = express();

// Statc file access
app.use(express.static('public'));

// Server Port
const port = process.env.PORT || 8080;

// Home Page
app.get("/", function(req, res){
    res.sendFile(path.join(__dirname+'/views/home.html'));
});

// About Page
app.get("/about", function(req, res){
    res.sendFile(path.join(__dirname+'/views/about.html'));
});


// Employees Page
app.get("/employees", function(req,res) {
    dataService.getAllEmployees()
    .then(function(value) {
        res.json(value);
    })
    .catch(function(err) {
        res.json({message: err});
    });
});


// Managers Page
app.get("/managers", function(req,res) {
    dataService.getManagers()
    .then(function(value) {
        res.json(value);
    })
    .catch(function(err) {
        res.json({message: err});
    });
});


// Department Page
app.get("/departments", function(req,res) {
    dataService.getDepartments()
    .then(function(value) {
        res.json(value);
    })
    .catch(function(err) {
        res.json({message: err});
    });
});


// Handle 404 Page
app.use(function(req, res) {
    res.sendFile(path.join(__dirname+'/views/404.html'));
  });


// Run APP
dataService.initialize();
app.listen(port, function() {
        console.log("Express http server listening on port:"+ port);
});
