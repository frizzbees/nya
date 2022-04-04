import discord
from discord.ext import commands

class Startup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # event
    @commands.Cog.listener()
    async def on_ready(self):
        print("--------------------")
        print(self.bot.user.name)
        print(self.bot.user.id)
        print("--------------------")

def setup(bot):
    bot.add_cog(Startup(bot))
