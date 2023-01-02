# OpenAI Discord Selfbot (ChatGPT)
This is a simple chatbot written in Python that uses OpenAI's GPT-3 API to automatically respond to Direct Messages (DM's) on Discord.

You can download the Windows binary here:

https://github.com/enterv0id/ChatGPT-Discord-Selfbot/releases/



## Requirements

- Use Python 3.10.4 or higher
- Install requirements:

``py -3 -m pip install -U discord.py-self``

``py -3 -m pip install -U openai``

## Usage

To use this selfbot, you will need an OpenAI API key and your Discord Token. 
Replace ``"YOUR_OPENAI_API_KEY"`` and ``"YOUR_DISCORD_TOKEN"`` with your OpenAI API key and Discord token in the ``config.json`` file.

**Get your OpenAI API key from** 
https://beta.openai.com/account/api-keys

**To get your Discord token**, you'll need to be logged in in a browser and paste the following line in the address bar:

``javascript:alert((webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken());``

You can select and copy your token displayed in the alert window.

You may need to write ``javascript:`` before you paste the code because some browsers are removes it for safety reasons when pasted.

**Note:** 

**Selfbots are against Discord's terms of service and should be used with caution. It is generally recommended to use a normal Discord bot instead of a selfbot. Use of this selfbot is at your own risk. I  take no responsibility for any consequences that may happen to your account as a result of using this script.**
