# Discord Sleep Bot 😴

A Discord bot built with **Python** and `discord.py` that can schedule a delayed voice disconnect — perfect for moderation or self-disconnect timers.

---

## 🧠 Features

- ⏳ Disconnect yourself or another member after a delay  
- 💬 Simple text commands (`!sleep`, `!cancel`)  
- 🔒 Safe — minimal permissions needed  
- ☁️ Works perfectly on **Replit** or locally

---

## ⚙️ Commands

| Command | Description |
|----------|--------------|
| `!sleep` | Disconnects you after 2 seconds |
| `!sleep 10` | Disconnects you after 10 seconds |
| `!sleep @user` | Disconnects another user after 2 seconds |
| `!sleep @user 10` | Disconnects another user after 10 seconds |
| `!sleep <user_id> 10` | Disconnects user by ID |
| `!cancel` | Cancels any active sleep timer |

---

## 🚀 Setup Guide

### 1️⃣ Create a Discord Application
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **“New Application”**
3. Name it something like `timer_sleep`
4. Go to the **Bot** tab and click **“Add Bot”**

---

### 2️⃣ Get Your Bot Token
1. In the **Bot** tab, click **“Reset Token”**
2. Copy the token (you’ll use it in your `.env` file)
3. Under **Privileged Gateway Intents**, enable:
   - ✅ Message Content Intent  
   - ✅ Server Members Intent  

---

### 3️⃣ Invite the Bot to Your Server
1. Go to **OAuth2 → URL Generator**
2. Under **Scopes**, check:
   - `bot`
   - `applications.commands`
3. Under **Bot Permissions**, check:
   - `Read Messages / View Channels`
   - `Send Messages`
   - `Connect`
   - `Move Members`
4. Copy the generated URL and open it in your browser  
5. Select your server → **Authorize**

---

### 4️⃣ Host the Bot on Replit
1. Go to [Replit](https://replit.com)
2. Click **“+ Create Repl”** → choose **Python**
3. Paste in the code from this repository
4. Add your environment variable:
   - Go to the **“Secrets (lock icon)”**
   - Add a new secret:
     ```
     Key: DISCORD_TOKEN
     Value: your_discord_bot_token_here
     ```
5. Click **Run** → you should see:



---

### ▶️ Launching the Bot
Once you’ve set it up in Replit, you can easily use it any time:
- Just open your Replit project  
- Click **“Run”** to launch the bot  
- It will connect to Discord and start working immediately  

When you’re done, you can stop it by clicking **“Stop”** or closing the Replit tab.  
You can run it again whenever you need it!

---

## 🧩 Environment Variables

| Variable | Description |
|-----------|--------------|
| `DISCORD_TOKEN` | Your Discord bot token (from Developer Portal) |

---

## 🧰 Requirements

- Python 3.8+
- `discord.py` library
- `python-dotenv`

Install dependencies:
```bash
pip install -r requirements.txt
```


MIT License © 2025 [Chouikh Ghassen](https://github.com/Chouikh-Ghassen)
