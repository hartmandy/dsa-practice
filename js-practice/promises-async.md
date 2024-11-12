# Callbacks

- A callback is a function passed as an argument to another function
- This technique allows a function to call another function
- A callback function can run after another function has finished

* JavaScript functions are executed in the sequence they are called. Not in the sequence they are defined.

Sometimes you would like to have better control over when to execute a function. Suppose you want to do a calculation, and then display the result.

```js
function myDisplayer(some) {
  document.getElementById("demo").innerHTML = some;
}

function myCalculator(num1, num2, myCallback) {
  let sum = num1 + num2;
  myCallback(sum);
}

myCalculator(5, 5, myDisplayer);
```

- When you pass a function as an argument, remember not to use parenthesis.
  In the real world, callbacks are most often used with asynchronous functions.

# Asynchronous Functions

Functions running in parallel with other functions are called asynchronous

When using the JavaScript function setInterval(), you can specify a callback function to be executed for each interval:

```js
setInterval(myFunction, 1000);

function myFunction() {
  let d = new Date();
  document.getElementById("demo").innerHTML =
    d.getHours() + ":" + d.getMinutes() + ":" + d.getSeconds();
}
```

With asynchronous programming, JavaScript programs can start long-running tasks, and continue running other tasks in parallel. But, asynchronus programmes are difficult to write and difficult to debug. Because of this, most modern asynchronous JavaScript methods don't use callbacks. Instead, in JavaScript, asynchronous programming is solved using Promises instead.

# Promises

- "Producing code" is code that can take some time
- "Consuming code" is code that must wait for the result
- A Promise is an Object that links Producing code and Consuming code

```js
let myPromise = new Promise(function (myResolve, myReject) {
  // "Producing Code" (May take some time)

  myResolve(); // when successful
  myReject(); // when error
});

// "Consuming Code" (Must wait for a fulfilled Promise)
myPromise.then(
  function (value) {
    /* code if successful */
  },
  function (error) {
    /* code if some error */
  }
);
```

The Promise object supports two properties: state and result.

- While a Promise object is "pending" (working), the result is undefined.
- When a Promise object is "fulfilled", the result is a value.
- When a Promise object is "rejected", the result is an error object.

Promise.then() takes two arguments, a callback for success and another for failure. Both are optional, so you can add a callback for success or failure only.

```js
function myDisplayer(some) {
  document.getElementById("demo").innerHTML = some;
}

let myPromise = new Promise(function (myResolve, myReject) {
  let x = 0;

  // The producing code (this may take some time)

  if (x == 0) {
    myResolve("OK");
  } else {
    myReject("Error");
  }
});

myPromise.then(
  function (value) {
    myDisplayer(value);
  },
  function (error) {
    myDisplayer(error);
  }
);
```

## Callback vs Promise

Callback:

```js
setTimeout(function () {
  myFunction("I love You !!!");
}, 3000);

function myFunction(value) {
  document.getElementById("demo").innerHTML = value;
}
```

Promise:

```js
let myPromise = new Promise(function (myResolve, myReject) {
  setTimeout(function () {
    myResolve("I love You !!");
  }, 3000);
});

myPromise.then(function (value) {
  document.getElementById("demo").innerHTML = value;
});
```

# Async

The keyword async before a function makes the function return a promise:

```js
async function myFunction() {
  return "Hello";
}
// Is the same as:

function myFunction() {
  return Promise.resolve("Hello");
}
```
