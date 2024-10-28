### useState

```js
function Counter() {
  const [count, setCount] = useState(0);
  const increment = () => setCount(count + 1);
  return <button onClick={increment}>{count}</button>;
}
```

useState is a function that accepts a single argument. That argument is the initial state for the instance of the component. In our case, the state will start as 0. State can be defined as: data that changes over time.

```js
import React, { useState } from "react";

function InputField() {
  const [text, setText] = useState("");

  function handleInputChange(event) {
    setText(event.target.value);
  }

  return (
    <div>
      <input type="text" value={text} onChange={handleInputChange} />
      <p>Input text: {text}</p>
    </div>
  );
}

export default InputField;
```
