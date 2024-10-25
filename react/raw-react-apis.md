### Imperative vs Declarative Programming

Imperative programming is how you do something, and declarative programming is more like what you do.

React abstracts away the imperative browser API from you to give you a much more declarative API to work with.

### You need two JavaScript files to write React applications for the web:

React: responsible for creating React elements (kinda like document.createElement())

ReactDOM: responsible for rendering React elements to the DOM (kinda like rootElement.append())

### Here's a simple example of how to use the React createElement API:

element takes in type, props, and children

```html
<script type="module">
  import { createElement } from "/react.js";
  import { createRoot } from "/react-dom/client.js";

  const rootElement = document.getElementById("root");
  const element = createElement(
    "div",
    { className: "container" },
    "Hello World"
  );
  createRoot(rootElement).render(element);
</script>
```
