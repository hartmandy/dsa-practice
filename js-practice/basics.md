# Javascript Basics

## Variables

Variables are containers for storing values.
Variables must be identified with unique names, called identifiers which are case sensitive.
The equal sign (=) is an "assignment" operator and is used like: `x = 5` to assign the variable x to the value of 5.

- The var keyword was used in all JavaScript code from 1995 to 2015, only use if you have to support older browsers. The let and const keywords were added to JavaScript in 2015.
- let is used when the variable changes
- const is used if the value or type (arrays and objects) doesn't change

You can declare many variables in one statement.

```js
let person = "John Doe",
  carName = "Volvo",
  price = 200;
```

```js
let x = 2 + 3 + "5";
```

## Operators

Most Common Operators

- The Assignment Operator = assigns values
- The Addition Operator + adds values
- The Multiplication Operator \* multiplies values
- The Comparison Operator > compares values

All Types

- Arithmetic Operators are used to perform arithmetic on numbers
  - The numbers (in an arithmetic operation) are called operands.
  - The operation (to be performed between the two operands) is defined by an operator.

```
+	Addition
-	Subtraction
*	Multiplication
**	Exponentiation (ES2016, produces the same result as `Math.pow(x,y)`)
/	Division
%	Modulus (Remainder)
++	Increment
--	Decrement
```

- Assignment Operators assign values to variables

```
  - =
  - += (x += y same as x = y)
  - -= (x -= y same as x = x - y)
  - _= (x _= y same as x = x \* y)
  - /= (x /= y same as x = x / y)
  - %= (x %= y same as x = x % y)
  - **= (x **= y same as x = x \*\* y)
```

- Comparison Operators

```
  - == equal to
  - === equal value and equal type
  - != not equal
  - !== not equal value or not equal type
  - > greater than
  - < less than
  - >= greater than or equal to
  - <= less than or equal to
  - ? ternary operator
```

- String Operators

  - You can concatenate strings by adding them together
  - If you put a number in quotes, the rest of the numbers will be treated as strings, and concatenated.

- Logical Operators

```
- &&	logical and
- ||	logical or
- !	logical not
```

- Bitwise Operators

```
- &	AND
- | OR
- ~	NOT
- ^	XOR (used as 5 ^ 1)
- <<	left shift (0101 << 1	would be 1010)
- >>	right shift (	0101 >> 1	would be 0010)
- >>>	unsigned right shift (0101 >>> 1	would be 0010)
```

- Ternary Operators
  - Given a condition, an expression which is executed if truthy value (to left of colon) or falsy value (to right of colon)
  - Should also handle if null

condition ? exprIfTrue : expIfFalse;

```js
const beverage = age >= 21 ? "Beer" : "Juice";

const name = person ? person.name : "stranger";
```

- Type Operators
  - Used to determine the type of a variable or expression
  ```js
  typeof "John Doe"; // Returns "string"
  ```

## Data Types

- String

```js
const name = "John Doe";
```

- Number

```js
let x = 5;
let y = 5.55;
```

- Bigint
  - JavaScript BigInt is a new datatype (ES2020) that can be used to store integer values that are too big to be represented by a normal JavaScript Number.

```js
let x = BigInt("123456789012345678901234567890");
```

- Boolean

```js
let x = 5;
let y = 5;
let z = 6;
(x == y)(x == z); // First returns true, second returns false
```

- Undefined
  - A variable without a value, has the value undefined. The type is also undefined.
- Null
  - Expresses a lack of identification, indicating a variable points to no object, treated as falsy boolean
- Symbol
  - New in ES6, represents a unique and immutable value often used as a key for object properties to avoid naming collisions with other keys
  ```js
  const mySymbol = Symbol();
  const anotherSymbol = Symbol("description"); // Creates symbol with description
  ```
- Object

```js
// Object:
const person = { firstName: "John", lastName: "Doe" };

// Array object:
const cars = ["Saab", "Volvo", "BMW"];

// Date object:
const date = new Date("2022-03-25");
```

- The object data type can contain both built-in objects, and user defined objects:
- Built-in object types can be: objects, arrays, dates, maps, sets, intarrays, floatarrays, promises, and more.

### JS Objects

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
