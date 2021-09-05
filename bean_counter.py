# bot.py
import os
import random
import discord
from discord.ext import commands
from discord.utils import resolve_template
from dotenv import load_dotenv
from bean_market import Beans

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


bot = commands.Bot(command_prefix='!')
bot.beanBank=[]


#INIT EVENTS===================================================================
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

#LOGICISTIC FUNCTIONS========================================================
def getBeanValue():
    beanValue=8
    return beanValue
#/LOGICISTIC FUNCTIONS========================================================

#COMMANDS===================================================================
@bot.command(name='test')
async def on_message(message):
    print('{},{}'.format(message.author,message.author.id))

@bot.command(name='beanbank')
async def on_message(message):
    response=''

    value = Beans.getTotalbeans(bot.beanBank)
    branchBeans = Beans.totalBranchBeans(bot.beanBank)
    if value > 0:
        response='There are {} Beans in the Bank Authority\nThe First National Bank of Bean has {} beans'.format(value,branchBeans)
    else:
        response='There are No Beans from the Bean Authority.  Lilith we have a problem'
    await message.send(response)


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


