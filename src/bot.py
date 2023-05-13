import disnake
from disnake.ext import commands
from config import BOT_TOKEN


def main():
    intents = disnake.Intents.default()
    intents.guild_messages = True
    intents.members = True
    intents.message_content = True
    intents.moderation = True
    intents.bans = True
    intents.guilds = True
    intents.guild_reactions = True

    bot = commands.InteractionBot(intents=intents)

    """
    Every cog should have its path added to this list relative to this file
    Each item should be separated by full stops, eg. 'cogs.tools.x'
    """
    cog_list = []

    @bot.event
    async def on_ready():
        print("Client ready!")

    bot.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
