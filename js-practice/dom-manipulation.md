## JS HTML DOM

What is the HTML DOM?
The HTML DOM is a standard object model and programming interface for HTML. It defines:

- The HTML elements as objects
- The properties of all HTML elements
- The methods to access all HTML elements
- The events for all HTML elements

In other words: The HTML DOM is a standard for how to get, change, add, or delete HTML elements.

<hr>

HTML DOM methods are actions you can perform (on HTML Elements).

HTML DOM properties are values (of HTML Elements) that you can set or change.

The innerHTML property is useful for getting or replacing the content of HTML elements.

```js
<html>
  <body>
    <p id="demo"></p>
    <script>document.getElementById("demo").innerHTML = "Hello World!";</script>
  </body>
</html>
```

Changing HTML Elements

- `element.innerHTML =  new html content` - Change the inner HTML of an element
- `element.attribute = new value` - Change the attribute value of an HTML element
- `element.style.property = new style` - Change the style of an HTML element
- `element.setAttribute(attribute, value)` - Change the attribute value of an HTML element

Adding and Deleting Elements

- `document.createElement(element)` - Create an HTML element
- `document.removeChild(element)` - Remove an HTML element
- `document.appendChild(element)` - Add an HTML element
- `document.replaceChild(new, old)` - Replace an HTML element
- `document.write(text)` - Write into the HTML output stream
<hr>

Finding HTML Element by Id

The easiest way to find an HTML element in the DOM, is by using the element id.

```js
const element = document.getElementById("intro");
```

<hr>

Finding HTML Elements by CSS Selectors

If you want to find all HTML elements that match a specified CSS selector (id, class names, types, attributes, values of attributes, etc), use the querySelectorAll() method. This example returns a list of all <p> elements with class="intro".

```js
const x = document.querySelectorAll("p.intro");
```

<hr>

Event listeners

```js
element.addEventListener(event, function, useCapture);

element.addEventListener("click", function(){ alert("Hello World!"); });

```
