/*********************************************************************************
* WEB322 – Assignment 02
* I declare that this assignment is my own work in accordance with Seneca Academic Policy. No part
* of this assignment has been copied manually or electronically from any other source
* (including 3rd party web sites) or distributed to other students.
*
* Name: Jungwook Kweon  Student ID: ______________  Date: ________________
*
* Online (Heroku) Link: https://web-app-322.herokuapp.com/
*
********************************************************************************/ 
// File accesss module
var fs = require('fs');

// Global array to store value
var employees = [];
var departments = [];


// Node module exports
module.exports = {
    // Save data into global array
    initialize: function() {
        let promise = new Promise(function(resolve, reject) {
            // data/employee.json 
            fs.readFile('./data/employees.json','utf8',(err,data) => {
                if (err) {
                    reject("Unable to load employee data file!");
                } else {
                    // Save the data into employee array
                    employees = JSON.parse(data);
                    console.log("Employee Data loaded");

                    // data/department.json 
                    fs.readFile('./data/departments.json','utf8',(err,data) => {
                        if (err) {
                            reject("Unable to load department data file!");
                        } else {
                            // parse data into departments array
                            departments = JSON.parse(data);
                            console.log("Department data loaded");
                            resolve('All the data initalized');
                        }
                    });
                }
            });
        });

        return promise;
    },

    // Get All employees data
    getAllEmployees: function() {
        let promise = new Promise(function(resolve,reject) {
            if (employees.length > 0) {
                resolve(employees);
            } else {
                reject('0 employee found!');
            }
        });
        return promise;
    },
    
    // Get Managers from employee
    getManagers: function() {
        let managers = []; 
        let promise = new Promise(function(resolve, reject) {
            // Go into employee array
            for (let i = 0; i < employees.length; i++) {
                // Check if manager value is true
                if (employees[i].isManager == true)
                    managers.push(employees[i]);

                if (managers.length > 0) {
                    resolve(managers);
                } else {
                    reject("0 Manager found!");
                }
            }
        });

        return promise;
    },
    
    // Get Departments
    getDepartments: function() {
        let promise = new Promise(function(resolve,reject) {
            if (departments.length > 0) {
                resolve(departments);
            } else {
                reject("0 Departments found!");
            }
        });

        return promise;
    },
};