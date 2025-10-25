from dotenv import load_dotenv
import os

load_dotenv()

CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
#WHISPER_API_KEY = os.getenv("WHISPER_API_KEY")

if __name__ == "__main__":
    print("Claude API Key:", CLAUDE_API_KEY)