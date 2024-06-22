const htmlString = "<div><p>Hello, world!</p></div>";

// Format HTML string
const formattedHtmlString = prettier.format(htmlString, {
  parser: "html",
});

console.log(formattedHtmlString);
