/*********************************************************************************
* WEB322 – Assignment 02
* I declare that this assignment is my own work in accordance with Seneca Academic Policy. No part
* of this assignment has been copied manually or electronically from any other source
* (including 3rd party web sites) or distributed to other students.
*
* Name: Jungwook Kweon  Student ID: ______________ Date: ________________
*
* Online (Heroku) Link: https://web-app-322.herokuapp.com/
*
********************************************************************************/ 
// Importing modules
var express = require('express');
const path = require("path");
const multer = require("multer");
const fs = require("fs");
const bodyParser = require("body-parser");

// data service component
var dataService = require('./data_service');
// Initialize express app
var app = express();

// Statc file access
app.use(express.static('public'));

// getting error message body parser is depercated,
// so using express
//app.use(bodyParser.urlencoded({extended: true}));

app.use(express.urlencoded({extended:true}));

// Server Port
const port = process.env.PORT || 8080;

// Define storag info
const storage = multer.diskStorage({
    destination: "./public/images/uploaded",
    filename: function(req, file, cb){
        cb(null, Date.now() + path.extname(file.originalname));
    }
});

// Upload image
const upload = multer({storage: storage});

// Home Page
app.get("/", function(req, res){
    res.sendFile(path.join(__dirname+'/views/home.html'));
});

// About Page
app.get("/about", function(req, res){
    res.sendFile(path.join(__dirname+'/views/about.html'));
});

// Add image form page
app.get("/images/add", function(req, res){
    res.sendFile(path.join(__dirname+'/views/addImage.html'));
});

// POST image
app.post("/images/add", upload.single("imageFile"), (req, res)=>{
    res.redirect("/images");
});

// Get images 
app.get("/images", (req, res) => {
    fs.readdir("./public/images/uploaded", function(err, items){
        res.json({images: items});
    });
});

// Add employees form page
app.get("/employees/add", function(req, res){
    res.sendFile(path.join(__dirname+'/views/addEmployee.html'));
});

// Post employees
app.post("/employees/add", (req, res) => {
    dataService
      .addEmployee(req.body)
      .then(() => {
        res.redirect("/employees");
      })
      .catch((err) => {
        res.send(err);
      });
  });

// Employees Page
app.get("/employees", function(req,res) {
    if (req.query.status) {
        dataService.getEmployeesByStatus(req.query.status).then(function (data) {
          res.json(data);
        });
      } else if (req.query.department) {
        dataService
          .getEmployeesByDepartment(req.query.department)
          .then((data) => {
            res.json(data);
          })
          .catch((err) => {
            res.json({ message: err });
          });
      } else if (req.query.manager) {
        dataService
          .getEmployeesByManager(req.query.manager)
          .then((data) => {
            res.json(data);
          })
          .catch((err) => {
            res.json({ message: err });
          });
        } else if(req.query.num){
            dataService
            .getEmployeeByNum(req.query.num)
            .then((data) => {
              res.json(data);
            })
            .catch((err) => {
              res.json({ message: err });
            });

      } else {
        dataService
          .getAllEmployees()
          .then((data) => {
            res.json(data);
          })
          .catch((err) => {
            res.json({ message: err });
          });
      }
});

// GE single employee

app.get("/employees/:id", function (req, res) {
    dataService
      .getEmployeeByNum(req.params.id)
      .then((data) => {
        res.json(data);
      })
      .catch((err) => {
        res.json({ message: err });
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
