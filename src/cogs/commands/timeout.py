import disnake
from disnake.ext import commands


class Timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="timeout", description="Mute a member for a given amount of time."
    )
    @commands.default_member_permissions(mute_members=True)
    async def timeout(
        self,
        inter: disnake.AppCmdInter,
        user: disnake.Member,
        duration: int,
        unit: str = "m",
        reason: str = "Reason not specified",
    ):
        unit = unit[0]
        time = duration
        embed = disnake.Embed(title="Timeout")
        match unit.lower():
            case "m":
                duration *= 60
            case "h":
                duration *= 3600
            case "d":
                duration *= 86400
        try:
            if user.id == inter.user.id:
                embed.description = "You cannot mute yourself"
                await inter.response.send_message(embed=embed)
            elif user.id == self.bot.user.id:
                embed.description = "I cannot mute myself."
                await inter.response.send_message(embed=embed)
            elif user.guild_permissions.administrator == True:
                if user.id == inter.guild.owner_id:
                    embed.description = "I cannot mute the server owner."
                    await inter.response.send_message(embed=embed)
                else:
                    embed.description = "I cannot mute that user because they have administrator permissions."
                    await inter.response.send_message(embed=embed)
            elif duration <= 0:
                if user.current_timeout == None:
                    embed.description = f"{user._user} isn't muted."
                    await inter.response.send_message(embed=embed)
                else:
                    embed.description = f"{user._user}'s timeout has been removed."
                    await user.timeout(
                        duration=0, reason=reason
                    ) and await inter.response.send_message(embed=embed)
            else:
                if user.current_timeout == None:
                    if unit.lower() == "m":
                        if time == 1:
                            unit = "minute"
                        else:
                            unit = "minutes"
                    elif unit.lower() == "h":
                        if time == 1:
                            unit = "hour"
                        else:
                            unit = "hours"
                    embed.description = (
                        f"{user._user} has been timed out for {time} {unit}."
                    )
                    embed.add_field(name="Reason", value=reason)
                    await user.timeout(
                        duration=duration, reason=reason
                    ) and await inter.response.send_message(embed=embed)
                else:
                    embed.description = f"{user._user} is already timed out."
                    await inter.response.send_message(embed=embed)
        except Exception as e:
            embed.description = "An error has occurred."
            await inter.response.send_message(embed=embed)
            return e


def setup(bot):
    bot.add_cog(Timeout(bot))
