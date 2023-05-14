import disnake
from disnake.ext import commands
from disnake.ext.commands import Context
from config import BOT_TOKEN


def main():
    bot = commands.InteractionBot(intents=disnake.Intents.all())

    def load_cogs():
        cog_list = [
            "cogs.events.ready",
            "cogs.commands.tools.ping",
            "cogs.commands.moderation.nick",
        ]
        for cog in cog_list:
            bot.load_extension(cog)

    load_cogs()

    bot.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
