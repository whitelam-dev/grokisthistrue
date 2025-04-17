# grokisthistrue

A simple Discord bot that replies "yes" or "no" randomly when mentioned.

## Setup

1. Ensure you have Python 3.8+ installed.
2. Create and activate a virtual environment:
   - Windows PowerShell: `\.\venv\\Scripts\\Activate.ps1`
   - Bash (macOS/Linux): `source venv/bin/activate`
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy the example environment file and set your bot token:
   ```bash
   cp .env.example .env     # or copy manually on Windows
   ```
   Then open `.env` and replace `your_token_here` with your Discord bot token.
5. Run the bot:
   ```bash
   python bot.py
   ```

## Usage

Mention the bot in any channel with `@grokisthistrue`, and it will respond with "yes" or "no".