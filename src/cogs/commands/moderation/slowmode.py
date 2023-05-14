import disnake
from disnake import Option
from disnake.ext import commands


class Slowmode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="slowmode", description="Change the message cooldown in a channel."
    )
    @commands.default_member_permissions(manage_messages=True)
    @Option(
        name="duration",
        description="How long someone has to wait to send another message (seconds)",
        type=disnake.OptionType.integer,
        required=True,
    )
    async def slowmode(self, inter: disnake.AppCmdInter, duration):
        await inter.response.send_message(f"{duration} is pretty long")


def setup(bot):
    bot.add_cog(Slowmode(bot))
