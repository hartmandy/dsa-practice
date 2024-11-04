## useRef

useRef lets you reference a value that’s not needed for rendering.

The simplest way is to use the ref prop is by passing a callback:

```js
function MyDiv() {
  return (
    <div
      ref={(myDiv) => {
        console.log(`here's my div!`, myDiv);
        return function cleanup() {
          console.log(`my div is getting removed from the page!`, myDiv);
        };
      }}
    >
      Hey, this is my div!
    </div>
  );
}
```

### Returns

useRef returns an object with a single property:

current: Initially, it’s set to the initialValue you have passed. You can later set it to something else. If you pass the ref object to React as a ref attribute to a JSX node, React will set its current property.
On the next renders, useRef will return the same object.

Here's a simple example of using the ref prop with useRef:

```js
function MyDiv() {
  const myDivRef = useRef < HTMLDivElement > null;
  useEffect(() => {
    const myDiv = myDivRef.current;
    // myDiv is the div DOM node!
    console.log(myDiv);
  }, []);
  return <div ref={myDivRef}>hi</div>;
}
```

- The benefit of this API over the ref callback approach is that you can store the ref object in a variable and safely access it later within a useEffect callback or event handlers.
- After the component has been rendered, it's considered "mounted." That's when the useEffect callback is called and so by that point, the ref should have its current property set to the DOM node. So often you'll do direct DOM interactions/manipulations in the useEffect callback.
- Every element has a special ref prop (as shown above). You pass a ref to that prop and React will give you a reference to the thing that's created for that element.
