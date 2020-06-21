import discord
import asyncio

import config
import img

client = discord.Client()


async def change_status():
    await client.wait_until_ready()
    while client.is_ready():
        await client.change_presence(activity=discord.Game(name=f"!felicitatie", type=1))
        await asyncio.sleep(20)


@client.event
async def on_ready():
    print('Felicitatie bot op account: {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == '!felicitatie':
        img.draw_image("pf.png", message.author.avatar_url)
        file = discord.File("./banner.png", filename="banner.png")
        embed = discord.Embed()
        embed.set_image(url="attachment://banner.png")
        await message.channel.send(file=file, embed=embed)
        log_channel = client.get_channel(723605970915295283)
        file = discord.File("./banner.png", filename="banner.png")
        await log_channel.send(file=file, embed=embed)


client.loop.create_task(change_status())
client.run(config.TOKEN)