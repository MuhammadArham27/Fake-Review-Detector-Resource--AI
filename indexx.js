async function submitReview() {
  const review = document.getElementById('reviewInput').value;
  const productName = document.getElementById('productName').value;
  const rating = document.getElementById('rating').value;
  const resultBox = document.getElementById('result');

  resultBox.innerText = "Analyzing...";

  try {
    const response = await fetch('http://localhost:5000/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        review: review,
        product: productName,
        rating: rating
      })
    });

    const data = await response.json();
    resultBox.innerHTML = `
      <strong>Prediction:</strong> ${data.result}<br>
      <strong>Product:</strong> ${data.product}<br>
      <strong>Rating:</strong> ${data.rating}
    `;
  } catch (error) {
    resultBox.innerText = "Error: Could not connect to the server.";
  }
  fetch("http://localhost:5000/predict", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    review: review,
    product: productName,
    rating: rating
  })
})

}
