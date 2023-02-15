import discord
import json

client = discord.Client(intents=discord.Intents.all())
prefix = '?'
questions = {
    1: "How old are you?",
    2: "How are you today?",
    3: "What is 9+1?",
    4: "What is your name?"
}
max_questions = len(questions)

@client.event
async def on_message(message):
    if not message.content.startswith(prefix) or message.author.bot:
        return

    args = message.content[len(prefix):].split()
    command = args.pop(0).lower()

    if command == 'apply':
        try:
            user = await message.author.create_dm()
            await user.send("Hey! Your application has started. You have 300 seconds to complete it.")
            embed = discord.Embed(title=f'Question [{1}/{max_questions}]', description=questions[1])
            await user.send(embed=embed)
            application = {'userId': message.author.id}
            i = 1
            while i <= max_questions:
                response = await client.wait_for('message', check=lambda m: m.author == message.author and m.channel == user)
                application[f'question{i}'] = response.content
                if i == max_questions:
                    break
                i += 1
                embed = discord.Embed(title=f'Question [{i}/{max_questions}]', description=questions[i])
                await user.send(embed=embed)

            try:
                with open('applications.json', 'r') as f:
                    data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                data = []

            data.append(application)
            with open('applications.json', 'w') as f:
                json.dump(data, f)

            channel = client.get_channel(123456) # Replace with your channel ID, this is where application when done will get sent to.
            last_application = data[-1]
            embed = discord.Embed(title='Application: ' + message.author.display_name)
            for i in range(1, max_questions + 1):
                embed.add_field(name=f'Question {i}', value=last_application[f'question{i}'], inline=False)
            await channel.send(embed=embed)

            await user.send('Thank you for applying!')

        except Exception as e:
            print(e)

client.run('token')
