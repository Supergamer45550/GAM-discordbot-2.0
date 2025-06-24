from discord.ext import commands
import discord

class TestCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="test", description="Test command!")
    async def test(self, ctx: discord.ApplicationContext):
        await ctx.respond("Test command executed!")

def setup(bot):
    bot.add_cog(TestCommand(bot))
