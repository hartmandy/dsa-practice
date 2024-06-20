// Get the button element
const likeButton = document.getElementById("like-button");
const textElement = likeButton.querySelector(".text");
const heartElement = likeButton.querySelector(".heart");

// Function to simulate a backend service call
function fakeBackendCall() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve();
    }, 2000); // Simulate a 2 second delay
  });
}

// Function to toggle the liked state
async function toggleLike() {
  if (likeButton.classList.contains("loading")) {
    return; // Do nothing if already loading
  }

  // Show loading state
  likeButton.classList.add("loading");
  textElement.textContent = "Processing...";

  // Simulate backend call
  await fakeBackendCall();

  // Remove loading state
  likeButton.classList.remove("loading");

  // Toggle the 'liked' class on the button
  likeButton.classList.toggle("liked");

  // Change the button text based on the state
  if (likeButton.classList.contains("liked")) {
    textElement.textContent = "Liked";
    heartElement.textContent = "❤️";
  } else {
    textElement.textContent = "Like";
    heartElement.textContent = "❤️";
  }
}

// Add a click event listener to the button to trigger the toggle function
likeButton.addEventListener("click", toggleLike);
