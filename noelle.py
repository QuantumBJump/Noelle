import discord
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

client = discord.Client()
voice = None

def get_channel_id(server, name):
    for channel in server.channels:
        if channel.name == name:
            return channel.id

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------')

@client.event
async def on_message(message):
    
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, "Calculating messages...")
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    elif message.content.startswith('!join'):
        global voice
        channel_name = ' '.join(message.content.split()[1:])
        channel_to_join = client.get_channel(get_channel_id(message.server, channel_name))
        await client.send_message(message.channel, 'Joining channel: ' + channel_name)
        if client.is_voice_connected(message.server):
            voice = await voice.move_to(channel_to_join)
        else:
            voice = await client.join_voice_channel(channel_to_join)

client.run('MjkxMjAxMzkzNDYzOTE4NTk0.C6mB_A.khU5NicYbB_1-erIA7jwd4b5ydM')
