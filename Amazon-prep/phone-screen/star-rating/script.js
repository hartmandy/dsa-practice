const stars = document.querySelectorAll(".star");
const ratingValue = document.getElementById("rating-value");

stars.forEach((star) => {
  star.addEventListener("click", () => {
    const value = star.getAttribute("data-value");
    ratingValue.textContent = `Rating: ${value}`;
    stars.forEach((s) => s.classList.remove("selected"));
    star.classList.add("selected");
    let previousStar = star.previousElementSibling;
    while (previousStar) {
      previousStar.classList.add("selected");
      previousStar = previousStar.previousElementSibling;
    }
  });
});

stars.forEach((star) => {
  star.addEventListener("mouseover", () => {
    stars.forEach((s) => s.classList.remove("hover"));
    star.classList.add("hover");
    let previousStar = star.previousElementSibling;
    while (previousStar) {
      previousStar.classList.add("hover");
      previousStar = previousStar.previousElementSibling;
    }
  });
});

document.querySelector(".stars").addEventListener("mouseleave", () => {
  stars.forEach((star) => star.classList.remove("hover"));
});
