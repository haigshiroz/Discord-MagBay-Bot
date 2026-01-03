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
    
    if message.content.raw_mentions.contains(client.user.id):
        await message.channel.send('You mentioned me!')


client.run('your token here')
