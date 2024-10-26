### Simple Forms in React

```js
function App() {
  return (
    <form action="path/to/backend/route">
      <label htmlFor="username" name="Username" />
      <input id="username" name="username" />
      <button type="submit">Submit</button>
    </form>
  );
}
```

Here are the different input types you can use in HTML:

Button: <input type="button">
Checkbox: <input type="checkbox">
Color: <input type="color">
Date: <input type="date">
Datetime, local:<input type="datetime-local">
Email: <input type="email">
File: <input type="file">
Hidden: <input type="hidden">
Image:<input type="image">
Month: <input type="month">
Number: <input type="number">
Password: <input type="password">
Radio: <input type="radio">
Range: <input type="range">
Reset: <input type="reset">
Search: <input type="search">
Submit: <input type="submit">
Phone Number: <input type="tel">
Text: <input type="text">
Time: <input type="time">
URL: <input type="url">
Week: <input type="week">

Handling form submission of files (like photos) and different ways to set action to the form

```js
import { createRoot } from "react-dom/client";

function App() {
  function logFormData(formData: FormData) {
    console.log(Object.fromEntries(formData));
  }

  return (
    <form
      action={logFormData}
      // action="api/onboarding"
      // method="POST"
      // encType="multipart/form-data"
      // onSubmit={event => {
      // 	event.preventDefault()
      // 	const formData = new FormData(event.currentTarget)
      // }}
    >
      <div>
        // Select
        <label htmlFor="accountTypeSelection">Account Type:</label>
        <select id="accountTypeSelection" name="accountType">
          <option value="">--Please select an option--</option>
          <option value="admin">Admin</option>
          <option value="teacher">Teacher</option>
          <option value="parent">Parent</option>
          <option value="student">Student</option>
        </select>
      </div>
      // Radio
      <fieldset>
        <legend>Visibility:</legend>
        <label>
          <input name="visibility" type="radio" value="public" />
          Public
        </label>
        <label>
          <input name="visibility" type="radio" value="private" />
          Private
        </label>
      </fieldset>
      <div>
        <label htmlFor="usernameInput">Username:</label>
        <input id="usernameInput" name="username" />
      </div>
      <div>
        <label htmlFor="passwordInput">Password:</label>
        <input id="passwordInput" name="password" type="password" />
      </div>
      <div>
        <label htmlFor="ageInput">Age:</label>
        <input id="ageInput" name="age" type="number" min="0" max="200" />
      </div>
      <div>
        <label htmlFor="photoInput">Photo:</label>
        <input id="photoInput" name="photo" type="file" accept="image/*" />
      </div>
      <div>
        <label htmlFor="colorInput">Favorite Color:</label>
        <input id="colorInput" name="color" type="color" />
      </div>
      <div>
        <label htmlFor="startDateInput">Start Date:</label>
        <input id="startDateInput" name="startDate" type="date" />
      </div>
      <button type="submit">Submit</button>
    </form>
  );
}

const rootEl = document.createElement("div");
document.body.append(rootEl);
createRoot(rootEl).render(<App />);
```

In React, you use the defaultValue prop to set the default value of an input and the defaultChecked prop to set the default value of a checkbox or radio. The defaultValue should be a string (or it will be coerced to a string) that matches the format of the input.
