# Arrays

An array can hold many values under a single name, and you can access the values by referring to an index number.

```js
const cars = ["Saab", "Volvo", "BMW"];
```

You access an array element by referring to the index number:

```js
const cars = ["Saab", "Volvo", "BMW"];
let car = cars[0];
```

### toString()

The JavaScript method toString() converts an array to a string of (comma separated) array values.

### length property

The length property of an array returns the length of an array (the number of array elements).

```js
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let length = fruits.length;
```

### push property

The easiest way to add a new element to an array is using the push() method:

```js
const fruits = ["Banana", "Orange", "Apple"];
fruits.push("Lemon"); // Adds a new element (Lemon) to fruits
```

The Difference Between Arrays and Objects

- In JavaScript, arrays use numbered indexes.
- In JavaScript, objects use named indexes.
- You should use objects when you want the element names to be strings (text).
- You should use arrays when you want the element names to be numbers.

## Array Methods

- Array length returns the length (size) of an array
- Array toString() converts an array to a string of (comma separated) array values
- Array at() returns an indexed element from an array. `let fruit = fruits.at(2);`
- Array join() joins all array elements into a string. `fruits.join(" * ") // Banana * Orange * Apple * Mango`
- Array pop() removes the last element from an array
- Array push() adds a new element to an array (at the end)
- Array shift() removes the first array element and "shifts" all other elements to a lower index
- Array unshift() adds a new element to an array (at the beginning), and "unshifts" older elements
- Array delete() leaves undefined holes in the array. \*Use pop() or shift() instead
- Array concat() creates a new array by merging (concatenating) existing arrays
  - The concat() method does not change the existing arrays. It always returns a new array.
  - The concat() method can take any number of array arguments.
- Array copyWithin() copies array elements to another position in an array
  - The copyWithin() method overwrites the existing values.
  - The copyWithin() method does not add items to the array.
  - The copyWithin() method does not change the length of the array.
- Array flat() creates a new array with sub-array elements concatenated to a specified depth
  ```js
  const myArr = [
    [1, 2],
    [3, 4],
    [5, 6],
  ];
  const newArr = myArr.flat();
  // 1,2,3,4,5,6
  ```
- Arry flatMap() first maps all elements of an array and then creates a new array by flattening the array
- Array splice() can be used to add new items to an array; slices out a piece of an array and adds to it
  ```js
  const fruits = ["Banana", "Orange", "Apple", "Mango"];
  fruits.splice(0, 1);
  // Orange,Apple,Mango
  ```
  - The first parameter (0) defines the position where new elements should be added (spliced in).
  - The second parameter (1) defines how many elements should be removed.
  - The rest of the parameters are omitted. No new elements will be added.
- Array toSpliced()
  - The difference between the new toSpliced() method and the old splice() method is that the new method creates a new array, keeping the original array unchanged, while the old method altered the original array.
- Array slice() slices out a piece of an array into a new array

## Sorting methods

- The sort() method sorts an array alphabetically
- reverse() method reverses the elements in an array
- toSorted() safe way to sort an array without altering the original array
- toReversed() safe way to reverse an array without altering the original array
