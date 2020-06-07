import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name='', type=1))


@client.event
async def on_message(message):
    if message.content.startswith("76561198969579722"):
        await client.send_message(message.channel, "샌박3및8시간벤")
    if message.content.startswith("76561199028947184"):
        await client.send_message(message.channel, "지속적인룰위반8시간벤")
                              
                              
access_token = os.environ["BOT_TOKEN"]

client.run(access_token)
