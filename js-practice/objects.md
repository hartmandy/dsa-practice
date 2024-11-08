# JS Objects

- Objects are containers for Properties and Methods.
- Properties are named Values
- Methods are Functions stored as Properties.
- Properties can be primitive values, functions, or even other objects.
- Objects are mutable: They are addressed by reference, not by value.

Building an Object

- An object literal is a list of name:value (key:value) pairs inside curly braces {}.
- You can also create an object using new Object(), and then adds 4 properties, but it isn't commonly used.

```js
// Create an Object
const person = new Object();

// Add Properties
person.firstName = "John";
person.lastName = "Doe";
person.age = 50;
person.eyeColor = "blue";
```

Methods

- Methods are actions that can be performed on objects.
- Methods are function definitions stored as property values.

```js
const person = {
  firstName: "John",
  lastName: "Doe",
  id: 5566,
  fullName: function () {
    return this.firstName + " " + this.lastName;
  },
};
```

### Using Object.values()

Object.values() creates an array from the property values:

```js
const myArray = Object.values(person);
// John,30,New York
```

### Using Object.entries()

Object.entries() makes it simple to use objects in loops:

```js
const fruits = { Bananas: 300, Oranges: 200, Apples: 500 };

let text = "";
for (let [fruit, value] of Object.entries(fruits)) {
  text += fruit + ": " + value + "<br>";
}

// Bananas: 300
// Oranges: 200
// Apples: 500
```

### Using JSON.stringify()

JavaScript objects can be converted to a string with JSON method JSON.stringify().

```js
// Create an Object
const person = {
  name: "John",
  age: 30,
  city: "New York",
};

// Stringify Object
let myString = JSON.stringify(person);

// {"name":"John","age":30,"city":"New York"}
```

JSON.parse() turns a string into an object
