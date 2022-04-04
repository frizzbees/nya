import discord, time, os                                                          
from discord.ext import commands                                                          
from dotenv import load_dotenv                                                          
                                                          
load_dotenv()                                                          
bot = discord.ext.commands.Bot(command_prefix='!')                                                          
                                                          
for filename in os.listdir('./cogs'):                                                          
    if filename.endswith('.py'):                                                          
        bot.load_extension(f'cogs.{filename[:-3]}')                                                          


bot.run(os.getenv('TOKEN'))                                                          
                                                          