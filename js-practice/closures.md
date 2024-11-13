# Closures

Closures are JS functions that can access values outside of their own scope (curly braces)

```js
const name = "Cooper";

function SayName() {
  return `Hello  ${name}`;
}
```

With a normal function, the code needed and any variables/ state accessed is contained within itself. To run it is added to a queue and runs, then removes from the queue.

With a function like above, a closure is created which creates a place in memory that can be accessed later (heap). It is a function combined with it's outer state for a lexical environment. It requires more memory and computation.

One way to keep a leak from happening is to contain a closure inside of another function.

```js
function init() {
  var name = "Mozilla"; // name is a local variable created by init
  function displayName() {
    // displayName() is the inner function, that forms a closure
    console.log(name); // use variable declared in the parent function
  }
  displayName();
}
init();
```
