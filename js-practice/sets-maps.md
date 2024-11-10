# JS Sets

- \*Can't access with keys like arrays, accessed in order of insertion
- A JavaScript Set is a collection of unique values.
- Each value can only occur once in a Set.
- The values can be of any type, primitive values or objects.

Pass an array to the new Set() constructor:

- Initializes a set

```js
// Create a Set
const letters = new Set(["a", "b", "c"]);
```

The add() Method

- Adds to end of set

```js
letters.add("d");
letters.add("e");
```

- delete() can delete a value and clear() deletes all values

The has() Method

- Checks to see if value is in set

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

# JS Maps

- A Map holds key-value pairs where the keys can be any datatype.
- A Map remembers the original insertion order of the keys.

You can create a JavaScript Map by:

- Passing an Array to new Map()
- Create a Map and use Map.set()

### new Map()

```js
// Create a Map
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200],
]);
```

You can add elements to a Map with the set() method
The get() method gets the value of a key in a Map
also has all of the methods of sets, like delete(), has(), clear() and size()
