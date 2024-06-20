const data = [
  { name: "John Doe", age: 28, city: "New York" },
  { name: "Jane Smith", age: 34, city: "San Francisco" },
  { name: "Paul Johnson", age: 45, city: "Chicago" },
  { name: "Emma Wilson", age: 22, city: "Boston" },
];

const tableBody = document.querySelector("#data-table tbody");
const searchInput = document.getElementById("search");

function renderTable(data) {
  tableBody.innerHTML = "";
  data.forEach((item) => {
    const row = document.createElement("tr");
    row.innerHTML = `
            <td>${item.name}</td>
            <td>${item.age}</td>
            <td>${item.city}</td>
        `;
    tableBody.appendChild(row);
  });
}

function sortTable(column, order) {
  const sortedData = [...data].sort((a, b) => {
    if (a[column] > b[column]) {
      return order === "asc" ? 1 : -1;
    } else if (a[column] < b[column]) {
      return order === "asc" ? -1 : 1;
    } else {
      return 0;
    }
  });
  renderTable(sortedData);
}

function searchTable(query) {
  const filteredData = data.filter(
    (item) =>
      item.name.toLowerCase().includes(query.toLowerCase()) ||
      item.age.toString().includes(query) ||
      item.city.toLowerCase().includes(query.toLowerCase())
  );
  renderTable(filteredData);
}

document.querySelectorAll("th").forEach((header) => {
  header.addEventListener("click", () => {
    const column = header.getAttribute("data-column");
    const order = header.getAttribute("data-order");
    header.setAttribute("data-order", order === "asc" ? "desc" : "asc");
    sortTable(column, order);
  });
});

searchInput.addEventListener("input", () => {
  searchTable(searchInput.value);
});

// Initial render
renderTable(data);
