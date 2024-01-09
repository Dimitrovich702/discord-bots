```py
@client.event
async def on_ready():
    print('Bot ready')

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
                
                # winner's 
                embed = discord.Embed(title="Congratulations!", description=f"{guess.author.mention} is the winner of our prize!")
                embed.colour = discord.Color.blue()
                embed.set_thumbnail(url=message.author.avatar)
                embed.set_footer(text="Thank you for participating!")
                await message.channel.send(embed=embed)
            else:
                await message.channel.send(f"Oops! The correct number was {num}. Better luck next time. Guess again!")

client.run(TOKEN) ```
