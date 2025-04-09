# RBXDCPY
RBXDCPY is a Discord bot that allows you to check other player's and your public inventory. Note that it only works on public inventories. 

## How to run
1. Create your own application via discord developer portal via https://discord.com/developers/applications
2. Copy and paste your client secret key
3. Create a .env file with this format
   ```
   DISCORD_CLIENT_SECRET="your-secret-key"
5. Create your own .venv file
   ```bash
   python -m venv .venv
6. Activate the virtual environment
   Windows: 
   ```bash
   .venv\Scripts\activate
    ```
   Linux/MacOS:
   ```bash
   source .venv/bin/activate
   ```
7. Once activated run this command
   ```bash
   pip install -r requirements.txt
8. Once finished, run this command
   ```bash
   python main.py
   ```
   Or if you have a python 2 on your system
   ```bash
   python3 hello.py
   ```
