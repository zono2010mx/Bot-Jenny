import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='j-', description="¿Te puedo ayudar? :)", intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Usuaria de discord"))
    print('Holaaaaa')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("¿Eh? ¿Me llamaste? Usa **j-ayuda** para ver como interactuar conmigo (＾▽＾)／")

@bot.command()
async def ayuda(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Mira lo que puedo todo lo que puedo hacer :D \n\n **j-ping** - Comprueba que estoy en linea \n **j-saludo** - Te saludo ouo \n **j-suma** *[Numero1]* *[Numero2]* - Sumo dos numeros :o \n **j-ran** *[NumeroMenor]* *[NumeroMayor]* - dame un rango de numeros y te doy uno aleatorio. \n **j-miembros** - Te digo el numero de personas en este server.")
    await ctx.send(embed=embed)

@bot.command()
async def saludo(ctx):
    await ctx.send("Holiiiiiiiiii ¿Me dejas controlar tu servidor? ¿Porfis?(◕‿◕)")

@bot.command()
async def ping(ctx):
    await ctx.send("Si estoy viva >.<")

@bot.command()
async def suma(ctx, n1: int, n2: int):
    await ctx.send("¿No sabes sumar? el resultado es: " + str(n1 + n2))

@bot.command()
async def ran(ctx, n1: int, n2: int):
    try:
        await ctx.send("Escogo el numero: " + str(random.randint(n1, n2)))
    except ValueError:
        await ctx.send("¡Tu primer numero es mayor que el segundo! ¡Va al reves tontin (￣▽￣*)ゞ")

@bot.command()
async def miembros(ctx):
    for guild in bot.guilds:
       await ctx.send("Somos " + str(len(guild.members)) + " fantasticas personitas en el server")
       await ctx.send("Obviamente la más importante soy yo o( ❛ᴗ❛ )o")

bot.run('Token')
