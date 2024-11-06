## useId

The useId hook generates a unique and stable identifier (ID) that you can use for DOM elements.
Here's an example of how you can use the useId hook in a form component:

```js
function FormField() {
  const id = useId();
  return (
    <div>
      <label htmlFor={id}>Name:</label>
      <input id={id} type="text" />
    </div>
  );
}
```

Unlike useState or useEffect, useId does not accept any arguments and returns a single string value. There's no setter or updater function because the ID it provides is meant to be constant and unique throughout the component's lifecycle.

One important thing to call out is that you should never use useId to generate IDs for non-DOM elements, like keys in a list or unique keys for React elements. Those IDs should come from your data, not from useId.
