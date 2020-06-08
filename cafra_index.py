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
    if message.content.startswith("76561199060808072"):
        await client.send_message(message.channel, "서바룰위반경고1회")
    if message.content.startswith("76561199028524034"):
        await client.send_message(message.channel, "초식전투룰위반경고1회")
    if message.content.startswith("76561198867491797"):
        await client.send_message(message.channel, "샌박경고1회")
    if message.content.startswith("76561198993260318"):
        await client.send_message(message.channel, "샌박경고누적8시간벤")
    if message.content.startswith("76561198927513483"):
        await client.send_message(message.channel, "샌박경고누적12시간벤및및욕설72벤") 
        
                              
access_token = os.environ["BOT_TOKEN"]

client.run(access_token)
