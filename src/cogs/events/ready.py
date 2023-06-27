import disnake
from disnake.ext import commands
from datetime import datetime
from termcolor import colored


class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            print(
                f"{self.bot.user} ready on {datetime.utcnow().strftime('%D at %H:%M')} (UTC)"
            )
            await self.bot.change_presence(
                activity=disnake.Activity(
                    type=disnake.ActivityType.playing,
                    name="github.com/Oblong101/ToolBox-Bot",
                )
            )
        except Exception as e:
            print(colored(f"An error has occurred:\n{e}", "red", "on_black", ["bold"]))
            return e


def setup(bot):
    bot.add_cog(OnReady(bot))
