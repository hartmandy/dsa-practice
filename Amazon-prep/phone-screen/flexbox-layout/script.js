const navToggle = document.querySelector(".nav-toggle");
const navLinks = document.querySelector(".nav-links");

navToggle.addEventListener("click", () => {
  const expanded = navToggle.getAttribute("aria-expanded") === "true" || false;
  navToggle.setAttribute("aria-expanded", !expanded);
  navLinks.hidden = expanded;
});

navLinks.addEventListener("keydown", (event) => {
  if (event.code === "Escape") {
    navToggle.click();
    navToggle.focus();
  }
});

navLinks.addEventListener("click", (event) => {
  if (event.target.tagName.toLowerCase() === "a") {
    navToggle.click();
    navToggle.focus();
  }
});
