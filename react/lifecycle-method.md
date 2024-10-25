# React Lifecycle

An object goes through different events in its existence: creation, updating, and deletion. The lifecycle methods of React allow developers to manipulate that object during very specific times of that object’s life. To use the lifecycle methods, you have to use a React class component. Then, just define the method within the class.

### Historically, class components were used for managing state. But now, with hooks, functional components can do the same thing.

## constructor()

This is the first method that a React component will go through. It will only happen once. This method is only needed if you plan on altering the original constructor method or if you plan on setting state.

## render()

This is how a component will first mount. After the component is mounted, this method will be invoked whenever React’s virtual DOM detects a change.

This is the one method that has to exist within a React class component. Every other method is optional. This method must return one JSX element.

## componentDidMount()

Since a component can only be mounted once, this method will only be called one time and that is when the component is successfully mounted. Typically, fetch requests are made in this method.

## shouldComponentUpdate()

Perhaps you don’t want React to re-render after every little change. You can use this method to manually control when a component should update. Should return a boolean value.

## componentDidUpdate()

This method can be used when you want to send the update to another library or you want the update to trigger another event.

## componentWillUnmount()

This method is called right before a component is unmounted. If you have background fetch requests that have been happening every few seconds, this is the method where you can stop them.
