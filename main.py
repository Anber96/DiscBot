import discord as d

client = d.Client()

#On ready event

@client.event
async def on_ready():
    print('CLBot is now online')

@client.event
async def on_message(message):
    #To make sure that our bot doesn't reply to itself
    if(message.author == client.user):
        return

    #message.content contains the actual text of the message
    if(message.content == "Hola"):
        await message.channel.send('Amigo')
    
    if(message.content == "Cool"):
        #Add \ to U and change + to 000
        await message.add_reaction('\U0001F60E')
    #message.channel gives us which channel we are goind to be within

#This will trigger if an message is edited
@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} edit a message. \n'
        f'Before: {before.content} \n'
        f'After: {after.content} '

    )

@client.event
async def on_reaction_add(reaction,user):
    await reaction.message.channel.send(
        f'{user} reacted with {reaction.emoji}'
    )

##Add your token from Discord development portal
client.run()