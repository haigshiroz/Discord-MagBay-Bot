import random
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # Ignore messages from self
    if message.author == client.user:
        return

    if client.user.id in message.raw_mentions or "mica" in message.content.lower():
        await message.channel.send(random.choice(sentences))

with open("token.txt", "r", encoding="utf-8") as file:
    token = file.read()

with open("messagebank.txt", "r", encoding="utf-8") as file:
    sentences = [line.strip() for line in file if line.strip()]

client.run(token)
