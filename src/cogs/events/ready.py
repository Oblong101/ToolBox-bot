import disnake
from disnake.ext import commands
from datetime import datetime


class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.bot.user} ready on {datetime.utcnow().strftime('%D, at %H:%M')}")


def setup(bot):
    bot.add_cog(OnReady(bot))
