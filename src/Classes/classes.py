import disnake


class ErrorEmbed(disnake.Embed):
    def __init__(self):
        self.embed = super().__init__(
            title="Error", description="An error has occurred."
        )

    def add_error(self, embed: disnake.Embed, error: str or Exception, value: str):
        embed.add_field(name="The following error has occurred", value=error)
