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
        embed.add_field(name="Where can I download this?",value="You can download it from the github [here](https://github.com/PhazonicRidley/Assistance-Links).")
        await self.bot.say(embed=embed)
    @commands.command(pass_context=True)
    async def ub9s(self, ctx):
        """boot9strap updating guide link"""
        await self.bot.delete_message(ctx.message)
        embed = discord.Embed(title="How to update boot9strap", color=1710847)
        embed.description = "You can use [this](https://3ds.guide/updating-b9s) guide to update boot9strap to the latest version."
        embed.set_author(name="Plailect")
        embed.set_thumbnail(url="https://avatars3.githubusercontent.com/u/16979510?v=48&s=500")
        await self.bot.say("", embed=embed)
    @commands.command(pass_context=True)
    async def ua9lh(self, ctx):
        """arm9loaderhax to boot9strap update guide"""
        await self.bot.delete_message(ctx.message)
        embed = discord.Embed(title="How to update from arm9loaderhax to boot9strap", color=16718362)
        embed.description = "You can use [this](https://3ds.guide/a9lh-to-b9s) guide to update from A9LH to B9S."
        embed.set_author(name="Plailect")
        embed.set_thumbnail(url="https://avatars3.githubusercontent.com/u/16979510?v=48&s=500")
        await self.bot.say("", embed=embed)
    @commands.command(pass_context=True)
    async def region(self, ctx):
        """Guide for changeing the region on 3ds"""
        await self.bot.delete_message(ctx.message)
        embed = discord.Embed(title="How to change the region on your 3ds", color=16750848)
        embed.description = "You can use [this](https://3ds.guide/region-changing)"
        embed.set_thumbnail(url="https://avatars3.githubusercontent.com/u/16979510?v=48&s=500")
        embed.set_author(name="Plailect")
        await self.bot.say("", embed=embed)
        

def setup(bot):
    bot.add_cog(AssistanceLinks(bot))
