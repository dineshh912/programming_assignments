# Objectively Funcy

What we're doing today is writing functions that can manipulate the object passed in.

## Setup

* Fork
* Clone
* Install dependencies with `npm install`
* Run the tests with `npm run test`

## Tasks

* `getFirstName` - returns the value of the firstName property of the given person object
  * `getFirstName({firstName: 'Colin', lastName: 'Jaffe'}) // -> 'Colin'`
  * `getFirstName({firstName: 'Petra', lastName: 'Solano'}) // -> 'Petra'`
  
* `getLastName` - returns the value of the lastName property of the given person object
  * `getLastName({firstName: 'Colin', lastName: 'Jaffe'}) // -> 'Jaffe'`
  * `getLastName({firstName: 'Petra', lastName: 'Solano'}) // -> 'Petra'`
  
* `getFullName` - returns the value of the firstName property plus the lastName property with a space in the middle for the given person object
  * `getFullName({firstName: 'Colin', lastName: 'Jaffe'}) // -> 'Colin Jaffe'`
  * `getFullName({firstName: 'Petra', lastName: 'Solano'}) // -> 'Petra Solano'`
  
* `setFirstName` - changes the value of the firstName property of the given person object to the given value
  * `setFirstName({firstName: 'Colin', lastName: 'Jaffe'}, 'Redacted') // -> {firstName: 'Redacted', lastName: 'Jaffe'}`
  * `setFirstName({firstName: 'Petra', lastName: 'Solano'}, 'Anthony') // -> {firstName: 'Anthony', lastName: 'Solano'}`
  
* `setAge` - changes the value of the age property of the given person object to the given value
  * `setAge({firstName: 'Colin', lastName: 'Jaffe', age: 39}, 45) // -> {firstName: 'Colin', lastName: 'Jaffe', age: 45}`
  * `setAge({firstName: 'Petra', lastName: 'Solano', age: 29}, 35) // -> {firstName: 'Petra', lastName: 'Solano', age: 35}`
  
* `giveBirthday` - increments by 1 the age property of the given person object, or gives them an age of 1 if they don't have that property
  * `giveBirthday({firstName: 'Colin', lastName: 'Jaffe', age: 39}) // -> {firstName: 'Colin', lastName: 'Jaffe', age: 40}`
  * `giveBirthday({firstName: 'Petra', lastName: 'Solano', age: 29}) // -> {firstName: 'Solano', lastName: 'Solano', age: 30}`
  * `giveBirthday({firstName: 'Baby', lastName: 'Jaffe'}) // -> {firstName: 'Baby', lastName: 'Jaffe', age: 1}`
  
* `marry` - sets the marital status of both given people to `true` and sets each person's `spouseName` property to be the full name of the other

```
const person1 = {firstName: 'Colin', lastName: 'Jaffe', married: false}
const person2 = {firstName: 'Petra', lastName: 'Solano', married: false}
marry(person1, person2)
console.log(person1) // -> {firstName: 'Colin', lastName: 'Jaffe', married: true, spouseName: 'Petra Solano'}
console.log(person2) // -> {firstName: 'Petra', lastName: 'Solano', married: true, spouseName: 'Colin Jaffe'}
```

* `divorce` - changes the marital status to `false` and removes the `spouseName` property from both given people
```
const person1 = {firstName: 'Colin', lastName: 'Jaffe', married: true, spouseName: 'Petra Solano'}
const person2 = {firstName: 'Petra', lastName: 'Solano', married: true, spouseName: 'Colin Jaffe'}
divorce(person1, person2);
console.log(person1) // -> {firstName: 'Colin', lastName: 'Jaffe', married: false} 
console.log(person2) // -> {firstName: 'Petra', lastName: 'Solano', married: false}
```

## Tips

* For `getFullName`, don't set a `fullName` property on the given object. Just give the caller of the function back a new value based on the first name and last name
* For `giveBirthday`, you'll need to have some way to tell if the key `age` is already in the given person
* For `marry`, you can re-use your `getFullName` function in order to get each person's `spouseName`. Just pass in the person whose `fullName` you want, and you'll get back your new `spouseName` property
* Same as above for `divorce`; you'll need to research a way to REMOVE the key `spouseName` from the given people. Simply setting the properties to `undefined` or `null` won't be sufficient
