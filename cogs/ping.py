import discord
from discord.ext import commands

class Ping(commands.Cog, name="Ping"):
    """Ping Command"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping", aliases=["pong"])
    async def ping(self, ctx):
        """Show current bots latency in ms"""
        await ctx.send(f"{round(self.bot.latency * 1000)}ms")

def setup(bot):
    bot.add_cog(Ping(bot))
    print("Ping is loaded")