import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='.', intents=intents)
TOKEN = 'dont share your bot token'
@client.event
async def on_ready():
    print('is working ready')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('.guess'):
        num = random.randint(1, 503)  # Random number between 1 and 503
        await message.channel.send("I've chosen a magical number. Can you guess what it is?")
        
        winner = False  # Variable to track if someone has won
        
        while not winner:
            def check(m):
                return m.author == message.author and m.channel == message.channel and m.content.isdigit()

            guess = await client.wait_for('message', check=check)
            if int(guess.content) == num:
                winner = True  # Set winner to True to exit the loop
                
                # winner's crap
                embed = discord.Embed(title="Congratulations!", description=f"{guess.author.mention} is the winner of our prize!")
                embed.colour = discord.Color.blue()
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1129362642016936056/1181884016866111488/image.png?ex=6582ae43&is=65703943&hm=70feae06707fe747c3061b045829d8d778cda5693cf59e3bc4a47a7fe467fc51&=&format=webp&quality=lossless&width=468&height=436")
                embed.set_footer(text="Thank you for participating!")
     
                # here else if u lose then X why the number to test123 
                await message.channel.send(embed=embed)
            else:
                await message.channel.send(f"Oops! The correct number was {num}. Better luck next time. Guess again!")

client.run(TOKEN) 
