useEffect is a built-in hook that allows you to run some custom code after React renders (and re-renders) your component to the DOM. It accepts a callback function which React will call after the DOM has been updated:

```js
useEffect(() => {
  // your side-effect code here.
  // this is where you can interact with browser APIs for example
  doSomeThing();
  return function cleanup() {
    // if you need to clean up after your side-effect (like unsubscribe from an
    // event), you can do it here
    doSomeCleanup();
  };
}, [
  // this is where dependencies of your useEffect callback go
  dep1,
  dep2,
]);
```
