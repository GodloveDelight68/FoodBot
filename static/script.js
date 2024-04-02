document.addEventListener('DOMContentLoaded', function () {
    const chatBox = document.getElementById('chat-box');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');



    // Add event listener to input field for 'keyup' event
    userInput.addEventListener("keyup", function(event) {
        // Check if the 'Enter' key is pressed (keyCode 13)
        if (event.keyCode === 13) {
            // Trigger click event of the send button
            sendButton.click();
        }
    });

    sendButton.addEventListener('click', function () {
        const userMessage = userInput.value.trim();
        if (userMessage !== '') {
            appendUserMessage(userMessage);
            sendUserMessage(userMessage);
            userInput.value = '';
        }
    });

    function appendBotMessage(message) {
        const div = document.createElement('div');
        div.className = 'chat-message bot-message';
        div.textContent = message;
        chatBox.appendChild(div);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function appendUserMessage(message) {
        const div = document.createElement('div');
        div.className = 'chat-message user-message';
        div.textContent = message;
        chatBox.appendChild(div);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function sendUserMessage(message) {
        fetch('/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                question: message
            })
        })
        .then(response => response.json())
        .then(data => {
            appendBotMessage(data.answer);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
});
