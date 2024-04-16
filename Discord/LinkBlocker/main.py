import discord
api=open('.env').read()
intents = discord.Intents.default()
intents.message_content = True

blacklist = ['discord.gg/','https://discord.gg/']
instaban= ['BanMe','teensleaked']

role = 1217837822812225567
staff = 1033009578528489584
logChannel = 1033014771655659523


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.author.get_role(role):
        return
        
    print(f'{message.author}:{message.content}')
    for word in message.content.split():
        for black in blacklist:
            if word[:len(black)] == black:
                logs = client.get_channel(logChannel)
                embed = discord.Embed()
                embed.add_field(name=f'{message.author.name}: {message.author.id}', value=message.content, inline=True)
                await logs.send(embed=embed)
                if word[len(black):] in instaban:
                    await message.delete()
                    await message.channel.send('NONO GET banned bad!')
                    await message.author.ban(reason='NO GET AWAY')
                else:
                    await message.delete()
                    await message.channel.send('Bad! no server invites here')

client.run(api)