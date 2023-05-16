import disnake
from disnake.ext import commands
from config import BOT_TOKEN


def main():
    bot = commands.Bot(command_prefix="%", intents=disnake.Intents.all())

    def load_cogs():
        cog_list = [
            "cogs.events.ready",
            "cogs.commands.tools.ping",
            "cogs.commands.moderation.nick",
            "cogs.commands.moderation.timeout",
            "cogs.commands.moderation.slowmode",
            "cogs.commands.moderation.ban",
            "cogs.commands.moderation.kick",
        ]
        for cog in cog_list:
            bot.load_extension(cog)

    load_cogs()

    bot.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
