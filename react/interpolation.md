## Template Literals

Template literals are literals delimited with backtick (`) characters, allowing for multi-line strings, string interpolation with embedded expressions, and special constructs called tagged templates.

Template literals are sometimes informally called template strings, because they are used most commonly for string interpolation (to create strings by doing substitution of placeholders). However, a tagged template literal may not result in a string; it can be used with a custom tag function to perform whatever operations you want on the different parts of the template literal.

### "Interpolation" is defined as "the insertion of something of a different nature into something else."

```js
const greeting = "Sup";
const subject = "World";
const message = `${greeting} ${subject}`;
```
