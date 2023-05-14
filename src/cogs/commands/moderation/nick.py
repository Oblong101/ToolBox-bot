import disnake
from disnake.ext import commands


class Nick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="nick", description="Apply a nickname to a user.")
    @commands.default_member_permissions(manage_nicknames=True)
    async def nick(
        self, inter: disnake.AppCmdInter, user: disnake.Member, nick: str = None
    ):
        try:
            if nick == None:
                embed = disnake.Embed(
                    title="Nickname",
                    description=f"{user.name}'s nickname has been reset.",
                )
                await user.edit(nick=None)
            elif user.guild_permissions.administrator == True:
                embed = disnake.Embed(
                    title="Nickname",
                    description=f"{user._user} has admin permissions. I cannot change their name.",
                )
            elif user._user == self.bot.user:
                embed = disnake.Embed(
                    title="Nickname",
                    description="You must change my nickname manually.",
                )
            elif nick == user.display_name:
                embed = disnake.Embed(
                    title="Nickname",
                    description="Couldn't update nickname. That is already their name.",
                )
            else:
                embed = disnake.Embed(
                    title="Nickname",
                    description=f"{user._user}'s nickname has been set to {nick}.",
                )
                await user.edit(nick=nick)
        except Exception as e:
            embed = disnake.Embed(description="An error has occurred.")
            await inter.response.send_message(embed)
            return e
        finally:
            await inter.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(Nick(bot))
