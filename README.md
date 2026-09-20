# CodeAlpha Chatbot 

## About the Project

This is a simple rule-based chatbot that I created as part of my **CodeAlpha Internship**.
I made this project using Python to practice basic programming concepts like functions, loops, if-else conditions, user input, and string handling.
The chatbot can understand a few basic messages and give predefined responses.

## How It Works

The chatbot starts by showing a welcome message and tells the user that they can type `quit` to exit.
Then it continuously takes input from the user using a `while` loop.

For example:

- If the user types `hello`, the bot replies **"Hi"**
- If the user types `how are you`, the bot replies **"I am fine, thank you for asking"**
- If the user types `quit`, the chatbot says goodbye and stops
- For any other message, the bot says **"Sorry, I don't understand"**

I used `.lower()` so that the input is converted into lowercase which makes it easier to compare the users message.
