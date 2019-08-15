import datetime
import discord
from os import getenv
from discord.ext import commands

description = 'Bot para mandar alertas dos boss do servidor South America'
bot = commands.Bot(command_prefix='.', description=description)
token = getenv('BOT_TOKEN')

@bot.event
async def on_ready():
    print('Bot ID: ', bot.user.id)
    print('Bot name: ', bot.user.name)
    print('---------------')
    print('This bot is ready for action!')

@bot.command()
async def ping(ctx):
    '''Returns pong when called'''
    author = ctx.message.author.name
    server = ctx.message.server.name
    await bot.send('Pong for {} from {}!'.format(author, server))

@bot.command()
async def peixinho():
	'''glub! '''
	await bot.send('_glub glub_')

@bot.command()
async def notifyme():
	'''Adiciona seu nome na lista de avisos'''
	author = ctx.message.author.name
	role = get(message.server.roles, name='Boss Timer')
	await client.add_roles(author, role)
	await bot.send('_glub glub_')

@bot.command()
async def removeme():
	'''Adiciona seu nome na lista de avisos'''
	author = ctx.message.author.name
	role = get(message.server.roles, name='Boss Timer')
	await client.remove_roles(author, role)
	await bot.send('_glub glub_')

bot.run(token)