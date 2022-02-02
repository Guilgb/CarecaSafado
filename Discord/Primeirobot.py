from email import message
from urllib import response
import discord
from discord.ext import commands


bot = commands.Bot("!")


@bot.event
async def on_ready():
    print(f"Estou pronto!! Meu bot é: {bot.user}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "palavrão" in message.content:
        await message.channel.send("Mensagem inapropiada")

        await message.delete()

    await bot.process_commands(message)


@bot.command(name="oi")
async def send_hello(ctx):
    name = ctx.author.name

    response = "Olá!" + name

    await ctx.send(response)
    # ultima linha do codigo
bot.run("OTM4NDkyOTIwNTkwMzc3MDUw.YfrFpA.5xMFWjvGax2jMILyAbT7UzbWHx8")
