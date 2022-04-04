import discord
from discord.ext import commands

class Status(commands.Cog, name="Status"):
    """Change Status"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="status", aliases=["stat"])
    async def status(self, ctx, *, status):
        """Allows server administrators to change the bots status"""
        if ctx.author.guild_permissions.administrator:
            await self.bot.change_presence(activity=discord.Game(status))
            await ctx.send(f"Changed status to {status}")
        else:
            await ctx.send("You do not have permission to change status!")

def setup(bot):
    bot.add_cog(Status(bot))
    print("Status is loaded")