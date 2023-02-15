# Discord Application Bot
Simple discord application bot, Made in Python

### FQA:

#### How to change the questions?

If you want to change the questions that are asked during the application process, you can do so by modifying the questions dictionary. Each question has a number as its key, and the question itself as its value. To change a question, simply update the corresponding value in the dictionary. For example, to change the second question to "What is your favorite color?", you would update the questions dictionary like this:

```python
questions = {
    1: "How old are you?",
    2: "What is your favorite color?",
    3: "What is 9+1?",
    4: "What is your name?"
}
```

#### How to change the Channel ID?

The code currently sends the completed application to a Discord channel with a specific ID. To change the channel ID, you need to replace the 123456 with the actual ID of the channel you want to use. You can find the ID of a channel by right-clicking on it and selecting "Copy ID". Then, replace 123456 with the copied ID.

```python
channel = client.get_channel(123456) # Replace with your channel ID
```

Make sure that the bot has permission to send messages to the channel that you select.
