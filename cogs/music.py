import asyncio
import functools
import itertools
import math
import random

import discord
import youtube_dl
from async_timeout import timeout
from discord.ext import commands

# 

def setup(bot):
    bot.add_cog(Music(bot))
    print('Music is loaded')