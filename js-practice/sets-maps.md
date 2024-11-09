# JS Sets

- A JavaScript Set is a collection of unique values.
- Each value can only occur once in a Set.
- The values can be of any type, primitive values or objects.

Pass an array to the new Set() constructor:

```js
// Create a Set
const letters = new Set(["a", "b", "c"]);
```

The add() Method

```js
letters.add("d");
letters.add("e");
```

The has() Method

```js
// Create a Set
const letters = new Set(["a", "b", "c"]);

// Does the Set contain "d"?
answer = letters.has("d");
```

The forEach() Method

- The forEach() method invokes a function for each Set element:

```js
// Create a Set
const letters = new Set(["a", "b", "c"]);

// List all entries
let text = "";
letters.forEach(function (value) {
  text += value;
});
```

The values() Method

- The values() method returns an Iterator object with the values in a Set:

```js
// Create a Set
const letters = new Set(["a", "b", "c"]);

// Get all Values
const myIterator = letters.values();

// List all Values
let text = "";
for (const entry of myIterator) {
  text += entry;
}
```
