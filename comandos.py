import random
import discord

#criei um comando que escolhe entre cara ou coroa
def moeda():
    lado = random.randint(1,2)
    if lado == 1:
        return 'cara'
    elif lado == 2:
        return 'coroa'

@bot.command()
async def CaraCoroa(ctx):
    resultado = moeda()
    await ctx.send(resultado)
