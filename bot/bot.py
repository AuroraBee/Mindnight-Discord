import discord
from discord import app_commands

# subclasses the discord.Client class
class LitepiClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id = '1013481020328251432'))
            self.synced = True
        print('------')
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        await self.change_presence(activity=discord.Game(name='with your mind at night~'))


# load the bot's token
with open('.config/token.txt', 'r') as f:
    token = f.readlines()
token = [x.strip() for x in token]
token = token[0]

bot = LitepiClient()
# Command tree
tree = app_commands.CommandTree(bot)
tree.clear_commands(guild = None)

# Test command that replies with "Hello!"
@tree.command(name = 'hello', description = 'Says hello!', guild=discord.Object(id = '1013481020328251432'))
async def hello(ctx: discord.Interaction):
    await ctx.response.send_message('Hello!', ephemeral=True)

bot.run(token)
