import disnake
from disnake.ext import commands
from typing import Optional


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
                await user.edit(nick=None) and await inter.response.send_message(
                    embed=embed
                )
            elif user.guild_permissions.administrator == True:
                embed = disnake.Embed(
                    title="Nickname",
                    description=f"{user._user} has admin permissions. I cannot change their name.",
                )
                await inter.response.send_message(embed=embed)
            elif user._user == self.bot.user:
                embed = disnake.Embed(
                    title="Nickname", description="You must change my nickname manually"
                )
                await inter.response.send_message(embed=embed)
            elif nick == user.display_name:
                embed = disnake.Embed(
                    title="Nickname",
                    description="Couldn't update nickname. That is already their name.",
                )
                await inter.response.send_message(embed=embed)
            else:
                embed = disnake.Embed(
                    title="Nickname",
                    description=f"{user._user}'s nickname has been set to {nick}.",
                )
                await user.edit(nick=nick)
                await inter.response.send_message(embed=embed)
        except Exception as e:
            embed = disnake.Embed(description="An error has occurred.")
            await inter.response.send_message(embed)
            return e
        await inter.response.send_message(f"{user.display_name} | {nick}")


def setup(bot):
    bot.add_cog(Nick(bot))
