import os
import random
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

import discord

# Configure intents to receive message content
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')


@client.event
async def on_message(message):
    # Ignore messages from bots (including itself)
    if message.author.bot:
        return
    # Reply to any message containing "fastkev"
    if 'fastkev' in message.content.lower():
        await message.channel.send("idk about that but fastkev is gay hahaha")
        return

    # Reply to any message containing "bad_stats" variants
    if any(keyword in message.content.lower() for keyword in ['bad_stats', 'bad stats', 'badstats']):
        await message.channel.send("idk about that but badstats is gay hahahahaha")
        return

    # Check if the bot is mentioned
    if client.user in message.mentions:
        response = random.choice(['yes', 'no'])
        await message.channel.send(response)


if __name__ == '__main__':
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        print('Error: DISCORD_TOKEN environment variable not set.')
        exit(1)

    client.run(token)