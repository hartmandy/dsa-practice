### Derived State

Derived state is state in an application that is not updated imperatively but instead inferred (computed) from a base state and/or other derived states or parts thereof.

```js
import { useState } from "react";

export default function Counter() {
  const [count, setCount] = useState(0);

  function handleClick() {
    const newCount = count + 1;
    setCount(newCount);
  }

  // this is the derived state
  const isEven = count % 2 === 0;

  return (
    <div>
      <p>{count}</p>
      <p>{isEven ? "Even" : "Odd"}</p>
      <button onClick={handleClick}>Increment</button>
    </div>
  );
}
```
