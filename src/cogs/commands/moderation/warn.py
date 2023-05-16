import disnake
from disnake.ext import commands
import sqlite3
import os


# connection = sqlite3.connect("caseinfo.db")
# cursor = connection.cursor()
# cursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS Warns
#     (Username TEXT, Reason TEXT)
#     """
# )
# connection.commit()
# connection.close()


class Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.connection = sqlite3.connect("caseinfo.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS warnings(user_id INTEGER, reason TEXT)"
        )
        self.connection.commit()
        self.connection.close()

    async def write_warn(self, user_id: int, reason: str):
        return

    @commands.slash_command(name="warn", description="Warn a member with a reason.")
    @commands.default_member_permissions(moderate_members=True)
    async def warn(self, inter: disnake.AppCmdInter, user: disnake.Member, reason: str):
        return


def setup(bot):
    bot.add_cog(Warn(bot))
