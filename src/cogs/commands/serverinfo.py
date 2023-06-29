import disnake, sys
from disnake.ext import commands


class PlaceholderClass(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="serverinfo", description="Fetch information about the server."
    )
    async def serverinfo(self, inter: disnake.AppCmdInter):
        """
        Fetch information about the server.

        Parameters
        ----------
        inter: Discord Application Interaction
        """
        guild_id = inter.guild.id
        membercount = len(inter.guild.members)
        await inter.response.send_message(membercount)


def setup(bot):
    bot.add_cog(PlaceholderClass(bot))
