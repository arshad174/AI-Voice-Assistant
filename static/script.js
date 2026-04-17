async function sendMessage() {
    let inputField = document.getElementById("userInput");
    let message = inputField.value;

    if (message.trim() === "") return;

    let chatbox = document.getElementById("chatbox");

    // Show user message
    chatbox.innerHTML += "<p><b>You:</b> " + message + "</p>";

    try {
        let response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        let data = await response.json();

        chatbox.innerHTML += "<p><b>Assistant:</b> " + data.response + "</p>";
    } catch (error) {
        chatbox.innerHTML += "<p style='color:red;'>Error connecting to server</p>";
        console.error(error);
    }

    inputField.value = "";
}