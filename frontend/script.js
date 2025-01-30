function sendRequest() {
    const userInput = document.getElementById("userInput").value;
    if (!userInput.trim()) {
        alert("Please enter a query!");
        return;
    }

    fetch("http://127.0.0.1:5000/chat", { 
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ prompt: userInput })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").innerHTML = `<p><strong>Forest:</strong> ${data.response}</p>`;
        document.getElementById("response").style.opacity = "1";  // Ensure animation triggers
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("response").innerHTML = "<p>Something went wrong.</p>";
    });
}
