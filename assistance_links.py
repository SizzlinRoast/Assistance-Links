import discord
from discord.ext import commands

'''General commands to use for 3DS assistance.'''



class AssistanceLinks:

    def __init__(self, bot):
        self.bot = bot

        async def simple_embed(self, text, title="", color=discord.Color.default()):
            embed = discord.Embed(title=title, color=color)
            embed.description = text
            await self.bot.say("", embed=embed)
		
    @commands.command(aliases=['pinfo'], pass_context=True)
    async def information(self, ctx):
        """About this cog"""
        await self.bot.delete_message(ctx.message)
        embed = discord.Embed(title= "What is this cog for?")
        embed.description = "The purpose of this cog is to quickly provide useful links on the 3DS Homebrew discord server."
        embed.add_field(name="Where can I download this?",value="You can download it from the github [here](https://github.com/PhazonicRidley/My-Cog).")
        await self.bot.say(embed=embed)
    @commands.command(pass_context=True)
    async def ub9s(self, ctx):
        """Boot9Strap updating guide link"""
        embed = discord.Embed(title="How to update Boot9Strap")
        embed = discord.Embed(title="How to update Boot9Strap" color=1710847)
        embed = discord.description = "This guide is to help you update your B9S to the latest version. Click [here](https://3ds.guide/updating-b9s)for a link to guide."
        embed = discord.author = "Plailect"
        embed = discord.thumbnail ="https://avatars3.githubusercontent.com/u/16979510?v=4&s=400"
        await self.bot.say("", embed=embed)

def setup(bot):
    bot.add_cog(AssistanceLinks(bot))