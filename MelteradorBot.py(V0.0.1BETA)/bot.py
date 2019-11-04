import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('STATUS: ONLINE')
@client.event
async def on_member_join(member):
    print(f'{member} Servera hoş geldin!')
@client.event
async def on_member_remove(member):
    print(f'{member} Serverdan ayrıldı.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {client.latency * 1000}ms')


@client.command()
async def sa(ctx):
        await ctx.send('Aleyküm Selam!')

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

    @client.command()
    async def ban(ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)

    @client.command()
    async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return



client.run('NjIwNjg3ODY3NDk2MTAzOTM3.XcCNKA.Op2-BQXN5ucMLV9pOX_oY79ZGUM')
