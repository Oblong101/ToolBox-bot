import disnake
from disnake.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ping", description="Return bot ping.")
    async def ping(self, inter: disnake.AppCmdInter):
        try:
            bot_ping = self.bot.latency
            embed = disnake.Embed(
                title="Ping", description=f"Bot Ping: {bot_ping:.4f}ms"
            )
            await inter.response.send_message(embed=embed)
            return bot_ping
        except Exception as e:
            embed = disnake.Embed(description="An error has occurred.")
            await inter.response.send_message(embed=embed)
            return e


def setup(bot):
    bot.add_cog(Ping(bot))
