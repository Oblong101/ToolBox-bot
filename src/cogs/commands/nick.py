import disnake
from disnake.ext import commands


class Nick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="nick")
    @commands.default_member_permissions(manage_nicknames=True)
    async def nick(
        self, inter: disnake.AppCmdInter, user: disnake.Member, nick: str = None
    ):
        """
        Apply a nickname to a user.

        Parameters
        ----------
        inter: Discord Application Interaction.
        user: The user who's nickname should be changed.
        nick: The user's new nickname.
        """
        embed = disnake.Embed(title="Nickname")
        try:
            if nick == None:
                embed.description = f"{user.name}'s nickname has been reset."
                await user.edit(nick=None)
                await inter.response.send_message(embed=embed)
            elif user.guild_permissions.administrator == True:
                embed.description = (
                    f"{user._user} has admin permissions. I cannot change their name."
                )
                await inter.response.send_message(embed=embed)
            elif user._user == self.bot.user:
                embed.description = "You must change my nickname manually."
                await inter.response.send_message(embed=embed)
            elif nick == user.display_name:
                embed.description = (
                    "Couldn't update nickname. That is already their name."
                )
                await inter.response.send_message(embed=embed)
            else:
                embed.description = f"{user._user}'s nickname has been set to {nick}."
                await user.edit(nick=nick)
                await inter.response.send_message(embed=embed)
        except Exception as e:
            embed.description = "An error has occurred."
            await inter.response.send_message(embed)
            return e


def setup(bot):
    bot.add_cog(Nick(bot))
