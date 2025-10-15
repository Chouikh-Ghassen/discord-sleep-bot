# Discord Sleep Bot 😴

A Discord bot built with `discord.py` that can schedule a delayed voice disconnect.
Perfect for moderation or self-disconnect timers.

## Commands
- `!sleep` → disconnects you (or a mentioned user) after a short delay
- `!cancel` → cancels an active timer
-     Disconnect yourself or another member after a delay.
    Usage:
-   ` !sleep `                -> disconnects YOU after 2 sec
-   ` !sleep 10 `             -> disconnects YOU after 10 sec
-   ` !sleep @user  `         -> disconnects @user after 2 sec
-   ` !sleep @user 10 `       -> disconnects @user after 10 sec
-   ` !sleep <user_id> 10 `   -> disconnects user by ID after 10 sec

## Setup
1. Clone the repo
2. Create a `.env` file with your bot token:
