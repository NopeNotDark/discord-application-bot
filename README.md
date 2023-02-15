# Discord Application Bot
This is a simple Discord bot that allows users to apply for something by answering a set of questions. The bot records the responses in a JSON file and sends a message to a specified channel with the answers.

## Configuration
To use the bot, you will need to create a Discord bot account and obtain its token. This can be done through the Discord Developer Portal.
Once you have the token, replace token in the last line of the code with your bot's token.
To send the application message to a specific channel, replace the 123456 in the line channel = client.get_channel(123456) with the ID of the channel you want to use.

## TODO:
- Add Review all Applications
- Send back Response from Application
- Remove Application if accepted or declined
- ~Add Lock and Unlock Application settings~

## USAGE:
After done setting up the token and channel id, run ?apply and check if the following questions can be answered.

### FQA:

If you are wondering what the `application.json` file is for, The applications.json file is used to store the responses that users provide during the application process. Each time a user completes an application, their responses are added to a list of applications in the JSON file.

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
