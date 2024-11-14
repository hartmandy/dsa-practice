# useReducer

useReducer is very similar to useState, but it lets you move the state update logic from event handlers into a single function outside of your component.

```js
const [state, dispatch] = useReducer(reducer, initialArg, init?)
```

Parameters

- reducer: The reducer function that specifies how the state gets updated. It must be pure, should take the state and action as arguments, and should return the next state. State and action can be of any types.
- initialArg: The value from which the initial state is calculated. It can be a value of any type. How the initial state is calculated from it depends on the next init argument.
- optional init: The initializer function that should return the initial state. If it’s not specified, the initial state is set to initialArg. Otherwise, the initial state is set to the result of calling init(initialArg).

```js
// outside of function
const countReducer = (count: number, change: number) => count + change;

// in function
const [count, changeCount] = useReducer(countReducer, initialCount);
const increment = () => changeCount(step);
const decrement = () => changeCount(-step);
```

If it needs to see the previous state to make new state, you can also write like this,

```js
const [state, setState] = useReducer(countReducer, {
  count: initialCount,
});
const { count } = state;
const increment = () =>
  setState((currentState) => ({ count: currentState.count + step }));
const decrement = () =>
  setState((currentState) => ({ count: currentState.count - step }));
```
