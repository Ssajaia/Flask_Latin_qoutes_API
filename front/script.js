const apiBaseUrl = "http://localhost:80";

document.getElementById("getQuote").addEventListener("click", () => {
  fetch(`${apiBaseUrl}/article/random`)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      document.getElementById("quote").textContent = data.quote;
    })
    .catch((err) => {
      document.getElementById("quote").textContent = "Error loading quote";
      console.error("Fetch failed:", err);
    });
});
