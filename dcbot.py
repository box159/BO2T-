import datetime
from http import client
import json
import requests
import discord
from discord.ext import commands
import keep_alive

client = commands.Bot(command_prefix='b!')

with open('config.json','r') as f:  
    odata = json.load(f)

def get_jokepng():
    resopnse = requests.get("https://memes.tw/wtf/api")
    data = json.loads(resopnse.text)
    num = odata["image"]["image_count"]
    day = datetime.datetime.now().day
    if(day != odata["image"]["day"]):
        odata["image"]["day"] = day
        num = 1

    if(num == len(data)):
        num = 1

    odata["image"]["image_count"]=num+1
    with open("config.json",'w') as f:
        json.dump(odata,f,indent=4) 

    return data[num]["src"]

def get_quote():
    response= requests.get("https://v1.hitokoto.cn/")
    json_data = json.loads(response.text)
    quote = json_data['hitokoto'] + '     -from ' + json_data["creator"]
    return(quote)

@client.event
async def on_ready():
    print("哈囉~我是",client.user)
    game = discord.Game("made by box159 | b!")
    await client.change_presence(status=discord.Status.online,activity=game)

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author == client.user:
        return
    if message.content=="b!":
        embed=discord.Embed(title="BO2T機器人指令表", description="--", color=0x00ff40)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/959065572799307797/960428136363876362/fixed.png")
        embed.add_field(name="b!", value="開啟指令介面", inline=False)
        embed.add_field(name="b!inspire", value="發送心靈雞湯", inline=False)
        embed.add_field(name="b!joke", value="發送梗圖", inline=False)
        embed.set_footer(text="made By box159#6942")
        await message.channel.send(embed=embed)
#         await message.channel.send("""           
# --------------------
# b! - 開啟指令介面
# b!inspire - 發送心靈雞湯
# b!joke - 發送梗圖
# --------------------
# """)
    elif message.content == 'ping':
        await message.channel.send('pong')
    elif message.content.startswith("說"):
        temp = message.content.split(" ",2)
        if(len(temp)==1):
            await message.channel.send("你要我說什麼啦？")
        else :
            await message.channel.send(temp[1])

@client.command()
async def ping(ctx):
    await ctx.send(round(client.latency*1000),'(ms)')

@client.command()    
async def joke(ctx):
    await ctx.send(get_jokepng())

@client.command() 
async def inspire(ctx):
    await ctx.send(get_quote())

@client.event
async def on_disconnect():
    await client.change_presence(status=discord.Status.offline)
try:
    alive = odata["keep_alive"]
    if(alive):
        keep_alive.keep_alive()
except:
    pass

client.run(odata["token"])