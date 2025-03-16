import discord
from discord.ext import commands
from discord import app_commands
import fetch_inventories
from settings import BOT_TOKEN
import pandas as pd
import asyncio

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event
    async def on_ready():
        print("Bot is ready!")

    @bot.command()
    async def sync(ctx):
        bot.tree.copy_global_to(guild=ctx.guild)
        await bot.tree.sync(guild=ctx.guild)
        await ctx.send("Synced!")
    
    @bot.command()
    async def ping(ctx):
        await ctx.send("Pong!")
        
    @bot.tree.command(name="inventory")
    @app_commands.describe(roblox_url="Your profile UID")
    async def inventory(ctx: discord.Interaction, roblox_url: str):
        try:
            messages = fetch_inventories.fetch_categories(roblox_url)
        except Exception as e:
            await ctx.response.send_message("An error occurred: " + str(e))
            return
        
        embed = discord.Embed(title="Inventory", description=f"Roblox item inventory for user {roblox_url}")

        items_per_page = 10
        pages = [messages[i:i+items_per_page] for i in range(0, len(messages), items_per_page)]
        current_page = 0
        total_pages = len(pages)

        embed.set_footer(text=f"Page {current_page+1} of {total_pages}")
        embed.add_field(name="Categories", value=f"```{pages[current_page]['Name'].to_string()}```", inline=False)

        await ctx.response.defer()
        message = await ctx.followup.send(embed=embed)

        await message.add_reaction("◀️")
        await message.add_reaction("0️⃣")
        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")
        await message.add_reaction("3️⃣")
        await message.add_reaction("4️⃣")
        await message.add_reaction("5️⃣")
        await message.add_reaction("6️⃣")
        await message.add_reaction("7️⃣")
        await message.add_reaction("8️⃣")
        await message.add_reaction("9️⃣")
        await message.add_reaction("▶️")

        def check(reaction, user):
            return user == ctx.user and str(reaction.emoji) in ["◀️", "0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "▶️"]
        
        while True:
            try:
                reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                break

            if str(reaction.emoji) == "◀️":
                current_page = max(current_page - 1, 0)
            elif str(reaction.emoji) == "▶️":
                current_page = min(current_page + 1, total_pages - 1)
            elif str(reaction.emoji) == "0️⃣":
                embed.clear_fields()
                embed.add_field(name="Items", value=fetch_inventories.fetch_inventory(roblox_url, pages[current_page]['ID'].iloc[0]))
                await message.edit(embed=embed)
                await message.remove_reaction(reaction.emoji, user)
                break
            elif str(reaction.emoji) == "1️⃣":
                embed.clear_fields()
                embed.add_field(name="Items", value=fetch_inventories.fetch_inventory(roblox_url, pages[current_page]['ID'].iloc[1]))
                await message.edit(embed=embed)
                await message.remove_reaction(reaction.emoji, user)
                break
            elif str(reaction.emoji) == "2️⃣":
                embed.clear_fields()
                embed.add_field(name="Items", value=fetch_inventories.fetch_inventory(roblox_url, pages[current_page]['ID'].iloc[2]))
                await message.edit(embed=embed)
                await message.remove_reaction(reaction.emoji, user)
                break
            elif str(reaction.emoji) == "3️⃣":
                embed.clear_fields()
                embed.add_field(name="Items", value=fetch_inventories.fetch_inventory(roblox_url, pages[current_page]['ID'].iloc[3]))
                await message.edit(embed=embed)
                await message.remove_reaction(reaction.emoji, user)
                break
            elif str(reaction.emoji) == "4️⃣":
                embed.clear_fields()
                embed.add_field(name="Items", value=fetch_inventories.fetch_inventory(roblox_url, pages[current_page]['ID'].iloc[4]))
                await message.edit(embed=embed)
                await message.remove_reaction(reaction.emoji, user)
                break
            elif str(reaction.emoji) == "5️⃣":
                embed.clear_fields()
                embed.add_field(name="Items", value=fetch_inventories.fetch_inventory(roblox_url, pages[current_page]['ID'].iloc[5]))
                await message.edit(embed=embed)
                await message.remove_reaction(reaction.emoji, user)
                break
            elif str(reaction.emoji) == "6️⃣":
                embed.clear_fields()
                embed.add_field(name="Items", value=fetch_inventories.fetch_inventory(roblox_url, pages[current_page]['ID'].iloc[6]))
                await message.edit(embed=embed)
                await message.remove_reaction(reaction.emoji, user)
                break
            elif str(reaction.emoji) == "7️⃣":
                embed.clear_fields()
                embed.add_field(name="Items", value=fetch_inventories.fetch_inventory(roblox_url, pages[current_page]['ID'].iloc[7]))
                await message.edit(embed=embed)
                await message.remove_reaction(reaction.emoji, user)
                break
            elif str(reaction.emoji) == "8️⃣":
                embed.clear_fields()
                embed.add_field(name="Items", value=fetch_inventories.fetch_inventory(roblox_url, pages[current_page]['ID'].iloc[8]))
                await message.edit(embed=embed)
                await message.remove_reaction(reaction.emoji, user)
                break
            elif str(reaction.emoji) == "9️⃣":
                embed.clear_fields()
                embed.add_field(name="Items", value=fetch_inventories.fetch_inventory(roblox_url, pages[current_page]['ID'].iloc[9]))
                await message.edit(embed=embed)
                await message.remove_reaction(reaction.emoji, user)
                break
            # Clear previous fields to avoid duplicate content
            embed.clear_fields()
            embed.add_field(name="Categories", value=f"```{pages[current_page]['Name'].to_string()}```", inline=False)
            embed.set_footer(text=f"Page {current_page+1} of {total_pages}")
            await message.edit(embed=embed)

            # Remove the user's reaction to avoid issues
            await message.remove_reaction(reaction.emoji, user)
            

        
        
    bot.run(BOT_TOKEN)
    

if __name__ == "__main__":
    run()