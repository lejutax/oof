import discord
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle

bot = commands.Bot(command_prefix = ".")
status = cycle(['Coding Server with \'.\'','by Anonyme#5137'])


@bot.event
async def on_ready():
    change_status.start()
    print('Mod is ready to be used')




#Commands to use
@bot.command(aliases=['h','assist','aide'])
async def command(ctx):                 
    await ctx.send('`Prefix to use` : \"**.**\"')
    await ctx.send('**.clear [amount of message to delete]** \n*delete specific number of messages*\n_e.g : **.clear 5**_\n --------------------')
    await ctx.send('**.cls** \n*clears chosen channel\'s chat*\n_e.g : **.cls**_\n --------------------')
    await ctx.send('**.kick [Player Tag]** \n*Kicks the player from the server*\n_e.g : **.kick Discord#0000** or **.kick @Discord**_\n --------------------')
    await ctx.send('**.ban [Player Tag]** \n*Bans the player from the server*\n_e.g : **.ban Discord#0000** or **.kick @Discord**_\n --------------------')
    await ctx.send('**.unban [Player Tag]** \n*Unbans the player from the server*\n_e.g : **.unban** or **Discord#0000**_\n --------------------')
    await ctx.send('**.e** *or* **.event ["Event"** + **"Date/Timing"**] \n*Create an event\'s announcement that contains an Event and its date/timing*\n_e.g : **.event** or **.e "Summer Travel to..." "17:00 am - Place"**_\n___USE QUOTES FOR **"EVENT"** and **"DATE"**, SEPARATED WITH SPACE___\n --------------------')
    await ctx.send('MORE FEATURES COMMING SOON\n --------------------')



@tasks.loop(seconds=3)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))


#CLEAR + ROLE NEEDED
@bot.command()
@commands.has_any_role('bot','Dad')
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit=amount)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send('You need \"**`Dad`**\" or \"**`bot`**\" role.')

        

#CLS + ROLE NEEDED
@bot.command()
@commands.has_any_role('Dad','bot')
async def cls(ctx, amount = 999999999999999999999999999999999999999999999999999999999999):
    await ctx.channel.purge(limit=amount)

@cls.error
async def cls_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send('You need \"**`Dad`**\" or \"**`bot`**\" role.')    






#REMOVE
@bot.command()
@commands.has_any_role('bot','Dad')
async def kick(ctx, member : discord.Member, *, reason = None ):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} was kicked from the server')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send('You need \"**`Dad`**\" or \"**`bot`**\" role.')


#ban
@bot.command()
@commands.has_any_role('bot','Dad')
async def ban(ctx, member : discord.Member, *, reason = None ):
    await member.ban(reason=reason)
    await ctx.send(f'{member.name}#{member.discriminator} was banned from the server')

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send('You need \"**`Dad`**\" or \"**`bot`**\" role.')



#unban
@bot.command(aliases=['uba'])
@commands.has_any_role('bot','Dad')
async def unban(ctx, *, member):
    banned_users_list = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    
    for ban_entry in banned_users_list:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} was unbanned')
            return

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send('You need \"**`Dad`**\" or \"**`bot`**\" role.')


#Annonce
@bot.command(aliases=['e', 'event'])
@commands.has_any_role('bot','Dad')
async def evenement(ctx, a, b):
    await ctx.send('```diff\n-Announcement:\n```\n```ini\n[Event: {}]\n```\n```json\n\"Date: {}\"\n```'.format(a.capitalize(),b.capitalize()))

@evenement.error
async def evenement_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send('You need \"**`Dad`**\" or \"**`bot`**\" role.')

bot.run('NzE4MjczNDU4MTI2OTc5MDgy.Xt2VXg.jFj2F1s3Jzix14yx8seWvKLRLSw')

