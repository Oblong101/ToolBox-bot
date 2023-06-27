import disnake
from disnake.ext import commands


class Slowmode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="slowmode",
        description="Change the message cooldown in a channel (in seconds).",
    )
    @commands.default_member_permissions(manage_messages=True)
    async def slowmode(
        self,
        inter: disnake.AppCmdInter,
        channel: disnake.TextChannel,
        duration: int,
    ):
        embed = disnake.Embed(title="Slowmode")
        try:
            embed.description = "Slowmode has been updated."
            embed.add_field(name="Channel", value=channel.mention)
            embed.add_field(name="Duration", value=f"{duration} seconds")
            await channel.edit(slowmode_delay=duration)
            await inter.response.send_message(embed=embed)
        except Exception as e:
            embed.description = "An error has occurred."
            await inter.response.send_message(embed=embed)
            return e


def setup(bot):
    bot.add_cog(Slowmode(bot))
