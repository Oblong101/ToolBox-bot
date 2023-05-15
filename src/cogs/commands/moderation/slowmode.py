import disnake
from disnake.ext import commands


class Slowmode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="slowmode", description="Change the message cooldown in a channel."
    )
    @commands.default_member_permissions(manage_messages=True)
    async def slowmode(
        self,
        inter: disnake.AppCmdInter,
        channel: disnake.TextChannel,
        duration: int,
    ):
        try:
            channel.edit(slowmode_delay=duration)
            await inter.response.send_message(
                f"{duration} is pretty long, {channel.id}"
            )
        except Exception as e:
            pass


def setup(bot):
    bot.add_cog(Slowmode(bot))
