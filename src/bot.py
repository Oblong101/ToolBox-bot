import disnake
from disnake.ext import commands
from config import BOT_TOKEN


def main():
    bot = commands.InteractionBot(intents=disnake.Intents.all())

    """
    Every cog should have its path added to this list relative to this file
    Each item should be separated by full stops, eg. 'cogs.tools.x'
    """
    cog_list = ["cogs.events.ready"]

    for cog in cog_list:
        bot.load_extension(cog)

    bot.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
