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
        embed.set_author(name="PhazonicRidley")
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
    @commands.command(aliases=['luma'], pass_context=True)
    async def Luma(self, ctx):
        """Links to Luma3ds versions 7.0.5, 7.1, and 8.1.1"""
        await self.bot.delete_message(ctx.message)
        embed = discord.Embed(title="Luma3ds download links", color=65535)
        embed.description = "Here are links to various Luma3ds versions make sure you click on the right version"
        embed.set_author(name="Aurora Wright")
        embed.set_thumbnail(url="https://gbatemp.net/attachments/luma3dsalt-png.46691/")
        embed.add_field(name="Luma3ds version 7.0.5", value="You can download Luma3ds 7.0.5 [here](https://github.com/AuroraWright/Luma3DS/releases/tag/v7.0.5).please note that this version of Luma is for ***arm9loaderhax users only***.")
        embed.add_field(name="Luma3ds version 7.1", value="You can download Luma3ds 7.1 [here](https://github.com/AuroraWright/Luma3DS/releases/tag/v7.1) please note that this version of Luma is only for boot9strap **1.0** users.")
        embed.add_field(name="Latest Luma3ds version", value="You can download the latest Luma3ds version [here](https://github.com/AuroraWright/Luma3DS/releases/latest).")
        await self.bot.say("", embed=embed)
    async def terms(self,ctx):
        """Link to Zeta's website; the information tab"""
        await self.bot.delete_message(ctx.message)
        embed = discord.Embed(title="3ds Hacking Terms", color=52224)
        embed.description ="Go [here](https://zetadesigns.github.io/info.html) to learn some basic terms about 3ds hacking."
        embed.set_author(name="Zeta")
        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/ouzBzyjEx0Xn2yh7rJ798UK3E543FDcl1S2xtxMxttw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/186474714124910592/6c0bd4dc9c043fe35c4b5f08dcdfaa80.webp?width=250&height=250")
        await self.bot.say("", embed=embed)
    @commands.command(pass_context=True)
    async def pokemon(self,ctx):
        """Pokemon game related guides"""
        await self.bot.delete_message(ctx.message)
        embed = discord.Embed(title="Here are some guides on how to randomize Pokemon games", color=10079487)
        embed.description = "These guides will help you randomize pokemon games and injecting pokemon prism save"
        embed.set_author(name="Slade and Zeta")
        embed.add_field(name="Randomizing a Pokemon game (CIA)",value="Go [here](https://zetadesigns.github.io/randomizing-cia.html) if you want to know how to randomize a CIA pokemon game.")
        embed.add_field(name="Randomizing a Pokemon game (LayeredFS)", value="Go [here](https://zetadesigns.github.io/randomizing-layeredfs.html) if want to randomize your pokemon game without creatingn a new cia.")
        embed.add_field(name="Injecting Pokemon Prism Save", value="Go [here](https://zetadesigns.github.io/injecting_prism.html) to inject pokemon prism saves.")
        await self.bot.say("", embed=embed)
    @commands.command(pass_context=True)
    async def ct(self,ctx):
        """"Cthulhu/Cashe Tool guide and download link"""
        await self.bot.delete_message(ctx.message)
        embed = discord.Embed(title="Cthulhu/Cashe Tool uses", color=993399)
        embed.description ="Go [here](https://github.com/Ryuzaki-MrL/CacheTool/releases/tag/1.3.2) to download Cthulu/Cashe Tool. You can also download it from FBI>TitleDB"
        embed.add_field(name="Cthulhu/CacheTool guide",value="Here are some uses and a guide for [Cthulhu/CacheTool](https://zetadesigns.github.io/cthulhu-usage.html)")
        embed.set_author(name="Slade and Zeta(guide),Lázaro Vieira(Cthulhu)")
        await self.bot.say("", embed=embed) 
    @commands.command(aliases=['fcp'], pass_context=True)
    async def flashcardpic(self,ctx):
        """compatibility list for what flashcards work and what dont for ntrboothax"""
        await self.bot.delete_message(ctx.message)
        embed = discord.Embed(title="compatibility list for ntrboothax")
        embed.set_image(url="https://cdn.discordapp.com/attachments/346830960668573697/346831110329860096/cart_list_V1.0.png")
        embed.set_author(name="EdTheNerd")
        await self.bot.say("", embed=embed)

        

def setup(bot):
    bot.add_cog(AssistanceLinks(bot))
