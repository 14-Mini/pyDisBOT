import discord
from discord import activity
from discord.enums import Status
from discord.ext import commands
from speedtest import Speedtest
from GoogleNews import GoogleNews
import wikipedia
import yfinance as yf
import random

#TOKEN=(ODU5ODI4NzgxNDY0MDI3MTc3.YNyX9A.bDPPUIJDlJa-mON50fmvk8qjcWI),though you can always regenrate this from 𝘥𝘦𝘷𝘦𝘭𝘰𝘱𝘦𝘳 𝘱𝘰𝘳𝘵𝘢𝘭 donot share this with anyone!

bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
    #custom bot status
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="Anime"))
    print("BOOM, booted up.")

@bot.command()
#only users with 'manage_messages' will be able to run this command
@commands.has_permissions(manage_messages=True)
async def clear(c, amount=5):  #anoumt - number of messages to be deleted by default.
    await c.channel.purge(limit=amount)

@bot.command(aliases=['k'])
@commands.has_permissions(kick_members=True)
async def kick(c, member:discord.Member, *, reason): #since reason is not set to None, you must give a reason to kick the user!
    try:
        await member.kick(reason=reason)
        await c.send(f'{member} 𝘩𝘢𝘴 𝘣𝘦𝘦𝘯 𝘬𝘪𝘤𝘬𝘦𝘥!')
    except:
        await c.send("Oops!! It seems that you don't have the power to invoke this command 𝘰𝘳 maybe the user you're using this command to has equal power as you!")

@bot.command(aliases=['b'])
@commands.has_permissions(ban_members=True)
async def ban(c, member:discord.Member, *, reason): #since reason is not set to None, you must give a reason to ban the user!
    try:
        await member.ban(reason=reason)
        await c.send(f'{member} 𝘩𝘢𝘴 𝘣𝘦𝘦𝘯 𝘣𝘢𝘯𝘯𝘦𝘥!')
    except:
        await c.send("Oops!! It seems that you don't have the power to invoke this command 𝘰𝘳 maybe the user you're using this command to has equal power as you!")

@bot.command()
async def roll(c):
    await c.send(f'{random.randint(0,100)},  (0-100).')

@bot.command()
async def flip(c):
    coin_sides= ['𝘏𝘌𝘈𝘋𝘚', '𝘛𝘈𝘐𝘓𝘚', '𝘒𝘖𝘓𝘛𝘌']
    await c.send(random.choice(coin_sides))

@bot.command(aliases=['spt'])
async def speed(c):
    await c.send("This might take few seconds, hold tight!")
    spt = Speedtest()
    download = (spt.download()/ 1048576)
    upload = (spt.upload()/ 1048576) 
    await c.send("Your Speed Details:")   
    await c.send(f'Download Speed = {download} mbps')
    await c.send(f'Upload Speed = {upload} mbps')

@bot.command()
async def news(c, *, newss):
    newss = newss
    googlenews = GoogleNews()
    googlenews = GoogleNews(period='7d')
    googlenews.search(newss)
    result = googlenews.result()
    for x in result:
        await c.send("-"*140)
        await c.send(f"Title--, {x['title']}")

        #somehow this img doesnt seem to work out so im commenting it out, you can undo this if you want
        #await c.send(f"Image--, {x['img']}")
        await c.send(f"Date/Time--, {x['date']}")
        await c.send(f"Description--, {x['desc']}")
        await c.send(f"Link--, {x['link']}")
        await c.send(f"Media--, {x['media']}")
        await c.send("-"*140)

@bot.command()
async def stock(c, *, stk):
    stk = stk
    cmnpy = yf.Ticker(stk)
    #gets stock info
    #await c.send(f'{cmnpy.info}')
    #gets hoistory of the stock
    await c.send(f'History of Stock {stk}.')
    await c.send('-'*140)
    hist = cmnpy.history(period='max')
    await c.send(hist)
    #get cashflow of the stock
    #cshflw = cmnpy.cashflow
    #q_cshflw = cmnpy.quarterly_cashflow
    #await c.send(cshflw)
    #await c.send(q_cshflw)
    #get the  recommendations from the analysists
    #recom = cmnpy.recommendations
    #await c.send('-'*140)
    #await c.send(recom)

@bot.command()
async def rstock(c, *, stk):
    stk = stk
    cmnpy = yf.Ticker(stk)
    #get the  recommendations from the analysists
    recom = cmnpy.recommendations
    await c.send(f"Recommendations from the Experts of the Stock {stk}.")
    await c.send('-'*140)
    await c.send(recom)

@bot.command()
async def wiki(c, *, search):
    search = search
    result = wikipedia.summary(f'{search}', sentences = 50)
    try:
        await c.send('-'*140)
        await c.send(result)
        await c.send('-'*140)
    except:
        await c.send("Something went wrong, this module didnt recognized the specific keyword!")
    




bot.run('ODU5ODI4NzgxNDY0MDI3MTc3.YNyX9A.bDPPUIJDlJa-mON50fmvk8qjcWI')
