import disnake, sys
from disnake.ext import commands

sys.path.append("../../Classes")
from Classes.classes import ErrorEmbed

error_embed = ErrorEmbed()


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ping")
    async def ping(self, inter: disnake.AppCmdInter):
        """
        Returns the bot's current ping.

        Parameters
        ----------
        inter: Discord Application Interaction
        """
        try:
            bot_ping = self.bot.latency
            embed = disnake.Embed(
                title="Ping", description=f"Bot Ping: {bot_ping:.4f}ms"
            )
            await inter.response.send_message(embed=embed)
            return bot_ping
        except Exception as e:
            error_embed.add_error(error=e, embed=error_embed)
            await inter.response.send_message(embed=error_embed)
            return e


def setup(bot):
    bot.add_cog(Ping(bot))
