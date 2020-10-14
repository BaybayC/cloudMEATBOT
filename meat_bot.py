import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = ";")

@client.event
async def on_ready():
    print("Ready to Int.")

@client.event
async def on_member_join(member):
    print(f'{member} has joined the meat gang.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the meat gang. f in the chat pls.')

@client.command()
async def ping(ctx):
    await ctx.send("Ripped and Ready")

@client.command(aliases=['weird'])
async def weird(ctx):
    await ctx.send(f'ULTIIIMAATEEECOOWWWLEVELL!!!')

client.run(os.environ['DISCORD_TOKEN'])

@client.command(aliases = ['fate'])
async def _8Ball(ctx, *, question):
    responses = ['Yuh bruh.',
                'Shhhhhiii maybe :)',
                'Yeahh.. Sike, nah.',
                'Seems weird, nah.',
                'Tis uncertain chief.',
                'I guess so...',
                'YES',
                'Absolutely, unimaginably no.',
                'Dududuudududududududu, YES indeed',
                'SICKO MODE YUH']
    await ctx.send(random.choice(responses))
