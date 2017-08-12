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
        embed.description = "You can use [this](https://3ds.guide/region-changing) guide to change the region of your 3ds"
        embed.set_thumbnail(url="https://avatars3.githubusercontent.com/u/16979510?v=48&s=500")
        embed.set_author(name="Plailect")
        await self.bot.say("", embed=embed)
    @commands.command(pass_context=True)
    async def Luma(self, ctx):
        """LInks to Luma3ds versions 7.0.5, 7.1, and 8.1.1"""
        await self.bot.delete_message(ctx.message)
        embed = discord.Embed(title="Luma3ds download links", color=65535)
        embed.description = "Here are links to various Luma3ds versions make sure you click on the right version"
        embed.set_author(name="Aurora Wright")
        embed.set_thumbnail(url="https://gbatemp.net/attachments/luma3dsalt-png.46691/")
        embed.add_field(name="Luma3ds version 7.0.5", value="You can download Luma3ds 7.0.5 [here](https://github.com/AuroraWright/Luma3DS/releases/tag/v7.0.5).please note that this version of Luma is for ***arm9loaderhax users only***.")
        embed.add_field(name="Luma3ds version 7.1", value="You can download Luma3ds 7.1 [here](https://github.com/AuroraWright/Luma3DS/releases/tag/v7.1) please note that this version of Luma is only for boot9strap **1.0** users.")
        embed.add_field(name="Luma3ds version 8.1.1", value="You can download Luma3ds version 8.1.1 [here](https://github.com/AuroraWright/Luma3DS/releases/tag/v8.1.1) this is the lastest version of Luma.")
        await self.bot.say("", embed=embed)
        

def setup(bot):
    bot.add_cog(AssistanceLinks(bot))
