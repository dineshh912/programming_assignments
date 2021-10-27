// Your code here.

// Get input person object and return only firstname
const getFirstName = function(person) {

    return person["firstName"];
}

// Get input person object and return only lastname
const getLastName = function(person) {

    return person["lastName"];
}

// Get input person and concat both firstname and lastname
const getFullName = function(person) {
    return `${person["firstName"]} ${person["lastName"]}`;
}

// Get person object and new firstname, need to replace person object firstname with new name
const setFirstName = function(person, name) {
    person["firstName"] = name;
}

// Get person object and new Age, need to replace person object Age with new age
const setAge = function(person, age) {
    person["age"] = age;
}

// Get person object, if age contains in the person increase age by 1 or return 1.
const giveBirthday = function(person) {

    if ("age" in person) {
        person["age"]++;
    } else {
        person["age"] = 1;
    }

}

// Set married property as true, and fill spouseName based on First name and last name
const marry = function(spouse1, spouse2) {
    spouse1.married = true;
    spouse2.married = true;

    spouse1.spouseName = `${spouse2.firstName} ${spouse2.lastName}`;
    spouse2.spouseName = `${spouse1.firstName} ${spouse1.lastName}`;
}

// Change the marrid property and remove spouseName

const divorce = function(spouse1, spouse2) {
    spouse1.married = false;
    spouse2.married = false;

    delete spouse1.spouseName;
    delete spouse2.spouseName;
}



// Our code here. Don't touch!
if (typeof getFirstName === 'undefined') {
    getFirstName = undefined
}

if (typeof getLastName === 'undefined') {
    getLastName = undefined
}

if (typeof getFullName === 'undefined') {
    getFullName = undefined
}

if (typeof setFirstName === 'undefined') {
    setFirstName = undefined
}

if (typeof setAge === 'undefined') {
    setAge = undefined
}

if (typeof giveBirthday === 'undefined') {
    giveBirthday = undefined
}

if (typeof marry === 'undefined') {
    marry = undefined
}

if (typeof divorce === 'undefined') {
    divorce = undefined
}


module.exports = {
    getFirstName,
    getLastName,
    getFullName,
    setFirstName,
    setAge,
    giveBirthday,
    marry,
    divorce,
}