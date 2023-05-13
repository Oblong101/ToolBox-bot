import disnake
from disnake.ext import commands


def bot():
    bot = commands.InteractionBot(intents=disnake.Intents.)

    """
    Every cog should have its path added to this list relative to this file
    Each item should be separated by full stops, eg. 'cogs.tools.x'
    """
    cog_list = []


