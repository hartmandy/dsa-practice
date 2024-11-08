# Conditional Statements

Very often when you write code, you want to perform different actions for different decisions.

### if

Use `if` to specify a block of code to be executed, if a specified condition is true

```js
if (condition) {
  //  block of code to be executed if the condition is true
}
```

<hr>

### else

Use `else` to specify a block of code to be executed, if the same condition is false

```js
if (condition) {
  //  block of code to be executed if the condition is true
} else {
  //  block of code to be executed if the condition is false
}
```

<hr>

### else if

Use `else if` to specify a new condition to test, if the first condition is false

```js
if (condition1) {
  //  block of code to be executed if condition1 is true
} else if (condition2) {
  //  block of code to be executed if the condition1 is false and condition2 is true
} else {
  //  block of code to be executed if the condition1 is false and condition2 is false
}
```

<hr>

### switch

Use `switch` to specify many alternative blocks of code to be executed. When JavaScript reaches a break keyword, it breaks out of the switch block.

```js
switch (expression) {
  case x:
    // code block
    break;
  case y:
    // code block
    break;
  default:
  // code block
}
```

Sometimes you will want different switch cases to use the same code.

```js
switch (new Date().getDay()) {
  case 4:
  case 5:
    text = "Soon it is Weekend";
    break;
  case 0:
  case 6:
    text = "It is Weekend";
    break;
  default:
    text = "Looking forward to the Weekend";
}
```

## Loops

Loops are handy, if you want to run the same code over and over again, each time with a different value.

JavaScript supports different kinds of loops:

- `for` - loops through a block of code a number of times
- `for/in` - loops through the properties of an object
- `for/of` - loops through the values of an iterable object
- `while` - loops through a block of code while a specified condition is true
- `do/while` - also loops through a block of code while a specified condition is true

### for loop

- Expression 1 is executed (one time) before the execution of the code block.
- Expression 2 defines the condition for executing the code block.
- Expression 3 is executed (every time) after the code block has been executed.

```js
for (let i = 0; i < 5; i++) {
  text += "The number is " + i + "<br>";
}
// Will loop through with i=0, iterating each time until reaching max of 4 (less than 5)
// The number is 0
// The number is 1
// The number is 2
// The number is 3
// The number is 4
// Then exiting loop
```

You can also set variables before the loop

```js
let i = 2;
let len = cars.length;
let text = "";
for (; i < len; i++) {
  text += cars[i] + "<br>";
}
```

Normally you will use expression 1 to initialize the variable used in the loop (let i = 0).

Often expression 2 is used to evaluate the condition of the initial variable. If expression 2 returns true, the loop will start over again. If it returns false, the loop will end.

Often expression 3 increments the value of the initial variable.

All are optional, though.

<hr>

### for in loop

The JavaScript for in statement loops through the properties of an Object:

```js
for (key in object) {
  // code block to be executed
}
```

```js
const person = { fname: "John", lname: "Doe", age: 25 };

let text = "";
for (let x in person) {
  text += person[x];
}
```

<hr>

### Array.forEach()

The forEach() method calls a function (a callback function) once for each array element.

```js
const numbers = [45, 4, 9, 16, 25];

let txt = "";
numbers.forEach(myFunction);

function myFunction(value, index, array) {
  txt += value;
}
```

Note that the function takes 3 arguments:

- The item value
- The item index
- The array itself

<hr>

### The For Of Loop

The JavaScript for of statement loops through the values of an iterable object. It lets you loop over iterable data structures such as Arrays, Strings, Maps, NodeLists, and more:

```js
for (variable of iterable) {
  // code block to be executed
}

const cars = ["BMW", "Volvo", "Mini"];
let text = "";
for (let x of cars) {
  text += x;
}
// BMW" "Volvo" "Mini
```

<b>The difference:</b>

- The `for...of` loop is designed to iterate over iterable objects, such as arrays, strings, maps, sets, and other iterable collections. (like const array = [10, 20, 30];)
- The `for...in` loop is is primarily used for iterating over the keys (or properties) of an object. It can also iterate over the indices of arrays (but this is not recommended for arrays). (like const obj = { a: 1, b: 2, c: 3 };)

```js
const array = ["a", "b", "c"];

// Using for...of
console.log("Using for...of:");
for (const value of array) {
  console.log(value); // Outputs: a, b, c
}

// Using for...in
console.log("Using for...in:");
for (const index in array) {
  console.log(index, array[index]); // Outputs: 0 a, 1 b, 2 c
}
```

<hr>

### The While Loop

The while loop loops through a block of code as long as a specified condition is true.

```js
while (condition) {
  // code block to be executed
}

while (i < 10) {
  text += "The number is " + i;
  i++;
}
```
