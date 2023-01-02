import discord
import openai
import asyncio
import platform
import sys
import os
import random
import json
import time


if sys.version_info < (3, 10, 4):
    # the version is not equal to 3.10.4 or bigger
    print("Error: Python 3.10.4 or higher is required to run this script.")
    # exit the script
    sys.exit()

delay = random.randint(3, 9)
if not os.path.exists("config.json"):
    print("Error: config.json is missing.")
    time.sleep(1)
    print("Generating new config.json")
    time.sleep(2)
    config_data = {
        "discord_token": "DISCORD_TOKEN",
        "openai_api_key": "OPENAI_API_KEY"
    }

    config_json = json.dumps(config_data, indent=4)

    with open("config.json", "w") as conf_file:
        conf_file.write(config_json)
    print("config.json created, please fill in your details and run the program again")
    time.sleep(1)
    print("Press CTRL+C to exit")
    time.sleep(5)
    exit()

with open("config.json", "r") as conf_file:
    conf_data = json.load(conf_file)

discord_token = conf_data["discord_token"]
openai_api_key = conf_data["openai_api_key"]
openai.api_key = openai_api_key

client = discord.Client(
    guild_subscription_options=discord.GuildSubscriptionOptions.off()
)

@client.event
async def on_ready():
    print(
        f"SelfBot logged in.\n \nUsername: {client.user}\nClient ID: {client.user.id}\nDiscord API Version: {discord.__version__}\nPython version: "
        + platform.python_version()
        + "\n\nSelfBot is up and running..."
    )


@client.event
async def on_message(message):
    if message.guild is None and message.author != client.user:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=message.content,
            max_tokens=1024,
            temperature=0.3,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        response_text = response["choices"][0]["text"]
        if response_text.strip():
            async with message.channel.typing():
                await asyncio.sleep(delay)
                await message.channel.send(response_text)


while True:
    try:
        response = openai.Completion.create(
            engine="text-davinci-003", prompt="Hi", max_tokens=1024
        )
        print("OpenAI API connected.")
        client.run(discord_token)
    except discord.errors.LoginFailure:
        print("\nError: Incorrect Discord token. Try again!")
        time.sleep(3)
    except openai.error.AuthenticationError:
        print("\nError: Invalid OpenAI API key. Try again!")
        time.sleep(3)

    break