JS Commands

- document.getElementById
- document.getElementById('root').innerHTML
- var x = document.getElementById("btn1").name

```html
<html>
  <body>
    <div id="root"></div>

    <script type="module">
      const rootElement = document.getElementById("root");
      const element = document.createElement("div");

      element.className = "container";
      element.textContent = "Hello World";

      rootElement.append(element);
    </script>
  </body>
</html>
```

Can also append

```html
<script type="module">
  const rootElement = document.createElement("div");
  rootElement.id = "root";

  const element = document.createElement("div");
  element.className = "container";
  element.textContent = "Hello World";

  rootElement.append(element);
  document.body.append(rootElement);
</script>
```

or modify

```html
<script>
  function changeText() {
    x = document.getElementById("mySelect");
    x.options[x.selectedIndex].text = "Melon";
  }
</script>
```
