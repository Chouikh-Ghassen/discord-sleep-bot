import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv
import logging
from typing import Optional

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Track active sleep tasks
active_sleep_task = None
sleep_task_info = None

@bot.event
async def on_ready():
    logger.info(f"Logged in as {bot.user}")
    print(f"Logged in as {bot.user}")

@bot.command()
async def sleep(ctx, arg1: Optional[str] = None, arg2: Optional[int] = None):
    """
    Disconnect yourself or another member after a delay.
    Usage:
    !sleep                 -> disconnects YOU after 2 sec
    !sleep 10              -> disconnects YOU after 10 sec
    !sleep @user           -> disconnects @user after 2 sec
    !sleep @user 10        -> disconnects @user after 10 sec
    !sleep <user_id> 10    -> disconnects user by ID after 10 sec
    """
    global active_sleep_task, sleep_task_info
    
    # Cancel any existing sleep task
    if active_sleep_task and not active_sleep_task.done():
        active_sleep_task.cancel()
        await ctx.send("Previous sleep request cancelled.")
    
    target = ctx.author
    seconds = 2

    if arg1:
        if arg1.isdigit():  # if it's a number → treat as seconds
            seconds = int(arg1)
        else:  # maybe it's a mention or user ID
            try:
                member = await commands.MemberConverter().convert(ctx, arg1)
                target = member
                if arg2:
                    seconds = arg2
            except commands.MemberNotFound:
                await ctx.send("I couldn't find that member. Try @mention or ID.")
                return

    # Store task info for cancellation
    sleep_task_info = {
        'target': target,
        'ctx': ctx,
        'seconds': seconds
    }
    
    await ctx.send(f"Okay, I'll disconnect {target.mention} in {seconds} seconds ⏳")
    
    # Create and store the sleep task
    active_sleep_task = asyncio.create_task(sleep_timer(ctx, target, seconds))
    
    try:
        await active_sleep_task
    except asyncio.CancelledError:
        # Task was cancelled, don't do anything
        pass
    finally:
        # Clean up
        active_sleep_task = None
        sleep_task_info = None

async def sleep_timer(ctx, target, seconds):
    """Separate function to handle the sleep timer"""
    await asyncio.sleep(seconds)
    
    target = ctx.guild.get_member(target.id)  # refresh state
    if target and target.voice:
        await target.move_to(None)
        await ctx.send(f"{target.mention} has been disconnected ✅")
    else:
        await ctx.send(f"{target.display_name} already left the voice channel.")

@bot.command()
async def cancel(ctx):
    """Cancel the current sleep request if there is one"""
    global active_sleep_task, sleep_task_info
    
    if active_sleep_task and not active_sleep_task.done():
        active_sleep_task.cancel()
        target_name = sleep_task_info['target'].display_name if sleep_task_info else "unknown user"
        await ctx.send(f"Sleep request for {target_name} has been cancelled ❌")
        active_sleep_task = None
        sleep_task_info = None
    else:
        await ctx.send("There is no request to cancel.")

@bot.event
async def on_command_error(ctx, error):
    """Handle command errors"""
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found! Use `!help` to see available commands.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required argument! Please check the command usage.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("I couldn't find that member. Try @mention or user ID.")
    else:
        logger.error(f"An error occurred: {error}")
        await ctx.send("An error occurred while processing the command.")

def main():
    """Main function to run the bot"""
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        logger.error("DISCORD_TOKEN not found in environment variables!")
        logger.info("Please set your Discord bot token using Replit's secrets management")
        return
    
    try:
        bot.run(token)
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")

if __name__ == "__main__":
    main()
