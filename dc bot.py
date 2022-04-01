from http import client
import json
from lib2to3.pgen2 import token
from unittest import case
from webbrowser import get
import requests
import discord
client = discord.Client()
with open('config.json') as f:  
    token = json.load(f)["token"]

def get_quote():
    response= requests.get("https://v1.hitokoto.cn/")
    json_data = json.loads(response.text)
    quote = json_data['hitokoto'] + '     -from ' + json_data["creator"]
    return(quote)

@client.event
async def on_ready():
    print("哈囉~我是",client.user)
    game = discord.Game("made by box159")
    await client.change_presence(status=discord.Status.online,activity=game)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("b2"):
        temp = message.content.split("b2",2)
        command = temp[1]
        if command == "?":
            await message.channel.send("""           
--------------------
b2? - 開啟指令介面
b2inspire - 發送心靈雞湯
--------------------
""")
        if command=="inspire":
            await message.channel.send(get_quote())
    if message.content == 'ping':
        await message.channel.send('pong')
    if message.content.startswith("說"):
        temp = message.content.split(" ",2)
        if(len(temp)==1):
            await message.channel.send("你要我說什麼啦？")
        else :
            await message.channel.send(temp[1])

@client.event
async def on_disconnect():
    await client.change_presence(status=discord.Status.offline)
client.run(token)