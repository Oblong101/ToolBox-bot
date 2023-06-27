import disnake
import os
from disnake.ext import commands
from config import BOT_TOKEN


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="%", intents=disnake.Intents.all())


bot = Bot()

print("EVENTS")
for f in os.listdir("./src/cogs/events"):
    if f.endswith(".py"):
        try:
            bot.load_extension(f"cogs.events.{f[:-3]}")
            print(f"Cog {f[:-3]} loaded")
        except Exception as e:
            print(
                f"An error has occurred while loading events: {e} => encountered in {f}"
            )
print("- - - - - - - -")

print("COMMANDS")
for f in os.listdir("./src/cogs/commands"):
    if f.endswith(".py"):
        try:
            bot.load_extension(f"cogs.commands.{f[:-3]}")
            print(f"Cog {f[:-3]} loaded")
        except Exception as e:
            print(
                f"An error has occurred while loading events: {e} => encountered in {f}"
            )
print("- - - - - - - -")


bot.run(BOT_TOKEN)
