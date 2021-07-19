import discord
from discord.ext import commands
from discord import User
from discord.ext.commands import Bot
import datetime

""" VARIABELEN """
client = Bot(command_prefix='!')
output_channel_id = #
spamChannel = #
bugChannel = #

@client.event
async def on_ready():
    try:
        print("Suggestion bot is ready to use")
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="your suggestions!"))

    except Exception as ex:
        print("exception found:")
        print(ex)
        embed = discord.Embed()
        embed.add_field(name="ERROR", value=str(ex))
        output = client.get_channel(bugChannel)
        await output.send(embed=embed, content=None)


@client.command(pass_context=True)
async def suggestion(ctx):
    if ctx.channel.id != spamChannel:
        return
    else:
        await ctx.message.delete(delay=2)
        emb=discord.Embed(title=f':bulb: Send us your input!',description='Send it as specific possible! You\'ll have **two** minutes to send the message. After that, you have to re-write ``!suggestions`` in {spamChannel}")
        await ctx.message.author.send(embed=emb)
        msg = await client.wait_for('message', check=lambda message: ctx.author == message.author and isinstance(message.channel, discord.DMChannel))

        if msg:
            suggestionChannel = client.get_channel(767357748731576341) # Embed will be sent to this channel
            userAvatar = msg.author.avatar_url
            emb=discord.Embed(title=':bulb: New Suggestion | Vote Now!', color=0x34e67f, description=str(msg.content),timestamp=datetime.datetime.utcnow())
            emb.set_footer(text=f'Submitted by {msg.author.name}', icon_url=str(userAvatar))
            try:
                sentEmbed = await suggestionChannel.send(embed=emb)
                await sentEmbed.add_reaction('✅')
                await sentEmbed.add_reaction('❌')
            except Exception as ex:
                embed = discord.Embed()
                embed.add_field(name="ERROR", value=str(ex))
                output = client.get_channel(bugChannel)
                await output.send(embed=embed, content=None)


client.run("TOKEN")
