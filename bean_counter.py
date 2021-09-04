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

@bot.command(name='givebean')
async def on_message(message, arg1):
    print('{},{}'.format(message.author,message.author.id))    
    await message.send('You sent {}'.format(arg1))

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
    


@bot.command(name='beanval')
async def bean_val(ctx):
    bv = getBeanValue()
    response = "Today, one bean is worth {} schmeckles".format(bv)
    await ctx.send(response)




#/COMMANDS===================================================================


bot.run(TOKEN)


