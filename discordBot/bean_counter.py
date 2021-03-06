# bot.py
import os
import random
from aiohttp.http import RESPONSES
import discord
from discord import message
from discord.ext import commands
from discord.utils import resolve_template
from dotenv import load_dotenv
from bean_market import Beans
import datetime

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')
bot.beanBank=[]




#=====
import threading
import time




async def test(message):
    while 1==1:
        currentTime = str(datetime.datetime.now())
        await printOut(f'{message} {currentTime}',737408433015226422)
        time.sleep(5)


async def printOut(message,channelID):

    channel = bot.get_channel(channelID)
    await channel.send("```"+message+"```")


#t1 = threading.Thread(target=test(message))

#=====


#LOGICISTIC FUNCTIONS=========================================================
def getBeanValue():
    beanValue=8
    return beanValue
def textFormat(message,option,color):
    formated=''
    return formated
#/LOGICISTIC FUNCTIONS========================================================

#INIT EVENTS==================================================================

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user} is connected to the following guilds:\n'
        f'{guild.name}(id: {guild.id})'
    )
    print('Importing the Bean Bank!')
    bot.beanBank=Beans.getBeanBank()
    #print(bot.beanBank)
    print('Bean Bank Imported!')
    member = await bot.fetch_user('176784920465768448')
    response=f'Bean bot has come online at {str(datetime.datetime.now())}\n'
    response=response+f'{bot.user} is connected to the following guilds:\n'
    response=response+f'{guild.name}(id: {guild.id})'
    #await t1("hi, im elfo")
    channel = bot.get_channel(737408433015226422)
    await channel.send("```"+response+"```")

   

@bot.command(name='embedtest')
async def embed(ctx):

    embed=discord.Embed()
    embed.title="This is a test"
    #(title="Sample Embed", url="https://cdn.discordapp.com/attachments/884556645655511080/884556972165333023/loose-change-450x300.jpg", description="This is an embed that will show how to build an embed and the different components", color=0xFF5733)
    embed.set_image(url="https://cdn.discordapp.com/attachments/884556645655511080/884556972165333023/loose-change-450x300.jpg")

    await ctx.send(embed=embed)





@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to the bean economy')


@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise
#/INIT EVENTS===================================================================


#COMMANDS===================================================================

@bot.command(name='beanbank')
async def on_message(message):
    response=''
    print(message)
    value = Beans.getTotalbeans(bot.beanBank)
    branchBeans = Beans.totalBranchBeans(bot.beanBank)
    if value > 0:
        response='There are {} Beans in the Bank Authority\nThe First National Bank of Bean has {} beans'.format(value,branchBeans)
        await message.send(response)

    else:
        response='There are No Beans from the Bean Authority.  Lilith we have a problem'
        embed=discord.Embed()
        embed.title="WE'RE OUT OF MONEY!?"
        embed.set_image(url="https://cdn.discordapp.com/attachments/884556645655511080/885998210986967140/lilithgaypaniccolor.png")
        await message.send(response,embed=embed)


@bot.command(name='give')
async def on_message(message, arg1, arg2):
    userid1=str(message.author.id)
    userid2=str(arg1[3:21])
    if userid1 == userid2:
        await message.send("Nice Try MORON. GET BEAN'D")
        return

    status1=Beans.findBeanAccount(bot.beanBank,userid1)
    status2=Beans.findBeanAccount(bot.beanBank,userid2)
    index1=status1[0]
    index2=status2[0]
    accountExist1=status1[1]
    accountExist2=status2[1]

    if not accountExist1 or not accountExist2:
        await message.send("One or more of entered accounts does not exist in the Bank of Bean")
        return
    bal1=Beans.getBeanBalance(bot.beanBank,index1)
    bal2=Beans.getBeanBalance(bot.beanBank,index2)

    print(status1,bal1)
    print(status2,bal2)

    if bal1 < int(arg2):
        await message.send("Hey you broke ass hoe, you dont have enough money")
        return

    print(bot.beanBank)

    Beans.withdrawlBeans(bot.beanBank,index1,int(arg2))
    Beans.depositBeans(bot.beanBank,index2,int(arg2))

    Beans.setBeanBank(bot.beanBank)
    Beans.beanLog(userid1,arg2,userid2)
    response='<@!{}> sent {} Beans to {}'.format(message.author.id, arg2,arg1)
    await message.send(response)
    


@bot.command(name='grant')
async def on_message(message, arg1, arg2):
    userid1=str(arg1[3:21])
    status=Beans.findBeanAccount(bot.beanBank,userid1)
    index1=status[0]
    accountExist1=status[1]

    if not accountExist1:
        await message.send("One or more of entered accounts does not exist in the Bank of Bean")
        return
    
    bal1=Beans.getBeanBalance(bot.beanBank,0)
    bal2=Beans.getBeanBalance(bot.beanBank,index1)

    if bal1 < int(arg2):
        await message.send("Hey you broke ass hoe, you dont have enough money")
        return

    Beans.withdrawlBeans(bot.beanBank,0,int(arg2))
    Beans.depositBeans(bot.beanBank,index1,int(arg2))

    Beans.setBeanBank(bot.beanBank)
    Beans.beanLog(69,arg2,userid1)
    response='The Bean Authority has given {} Beans to {}'.format(arg2,arg1)
    await message.send(response)









@bot.command(name='account')
async def on_message(message, arg1):
    response=''
    accountStatus=Beans.findBeanAccount(bot.beanBank,str(message.author.id))
    index=accountStatus[0]
    accountExists=accountStatus[1]

    if arg1 == 'status':
        if accountExists == True:
            response = '{}, you have {} Beans in your bean account'.format(message.author.display_name,bot.beanBank[index][2]) 
        else: 
            response = 'You do not have a bean account yet. Please create one'
    

    elif arg1 == 'create':
        if accountExists == False:
            bot.beanBank.append([message.author.name,str(message.author.id),str(0)])
            response= 'Account Created!'
            Beans.setBeanBank(bot.beanBank)
            bot.beanBank = Beans.getBeanBank()
            print(bot.beanBank)
        else:
            response = 'You already have an account.'

    else:
        response='Command not implemented'
    
    await message.reply(response)
    
@bot.command(name='request')
async def on_message(message, arg1, arg2):
    response='<@!{}> Requests {} Beans from {}'.format(message.author.id, arg2,arg1)
    await message.send(response)



@bot.command(name='beanval')
async def bean_val(ctx):
    bv = getBeanValue()
    response = "Today, one bean is worth {} schmeckles".format(bv)
    await ctx.send(response)




#/COMMANDS===================================================================


bot.run(TOKEN)


