import discord
import re
import os

# Get the token from the environment variable
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

if TOKEN is None:
    raise ValueError("No token found. Please set the DISCORD_BOT_TOKEN environment variable.")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Precompile the regex for better performance
url_pattern = re.compile(r'https?://(www\.)?(reddit\.com|instagram\.com|twitter\.com|youtube\.com|tiktok\.com|x\.com)')
ignore_patterns = re.compile(r'https?://(www\.)?(rxddit\.com|ddinstagram\.com|vxtwitter\.com|koutube\.com|vxtiktok\.com|fixupx\.com)')

# Dictionary for replacements
replacements = {
    'reddit.com': 'rxddit.com',
    'instagram.com': 'ddinstagram.com',
    'twitter.com': 'vxtwitter.com',
    'youtube.com': 'koutube.com',
    'tiktok.com': 'vxtiktok.com',
    'x.com': 'fixupx.com'
}

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    original_content = message.content

    # Check for the specific URLs to ignore
    if ignore_patterns.search(original_content):
        return

    # Function to perform replacement
    def replace_urls(match):
        domain = match.group(2)  # Extract the domain part
        return match.group(0).replace(domain, replacements.get(domain, domain))

    # Perform the substitution in one pass
    new_content = url_pattern.sub(replace_urls, original_content)

    # Only perform I/O operations if changes were made
    if new_content != original_content:
        #await message.channel.send(f'{message.author.mention} posted: {new_content}')
        await message.channel.send(f'{new_content}')

client.run(TOKEN)
