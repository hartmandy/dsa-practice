document.addEventListener("DOMContentLoaded", () => {
  const bookList = document.getElementById("bookList");
  const addBookBtn = document.getElementById("addBookBtn");

  // Fetch and display books on page load
  fetchBooks();

  // Event listener for add book button
  addBookBtn.addEventListener("click", handleAddBook);

  async function fetchBooks() {
    try {
      const response = await fetch("https://api.example.com/books");
      const books = await response.json();
      displayBooks(books);
    } catch (error) {
      console.error("Error fetching books:", error);
    }
  }

  function displayBooks(books) {
    bookList.innerHTML = "";
    books.forEach((book) => {
      const bookDiv = document.createElement("div");
      bookDiv.classList.add("book");
      bookDiv.innerHTML = `
                <h2>${book.title}</h2>
                <p>Author: ${book.author}</p>
                <p>${book.description}</p>
                <button onclick="handleEditBook(${book.id})">Edit</button>
                <button onclick="handleDeleteBook(${book.id})">Delete</button>
            `;
      bookList.appendChild(bookDiv);
    });
  }

  function handleAddBook() {
    // Code to handle adding a new book
    // This will involve displaying a form to input book details
    // and sending a POST request to the API
  }

  function handleEditBook(id) {
    // Code to handle editing a book
    // This will involve fetching the current book details,
    // displaying them in a form, and sending a PUT request to the API
  }

  function handleDeleteBook(id) {
    // Code to handle deleting a book
    // This will involve sending a DELETE request to the API
  }
});
