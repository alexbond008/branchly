import os 
from anthropic import Anthropic
from dotenv import load_dotenv





if __name__ == "__main__":

    load_dotenv()  # Load environment variables from .env file

    client = Anthropic(
        api_key=os.environ.get("CLAUDE_API_KEY")
    )

    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        messages=[
            {"role": "user", "content": "Hi there! Tell a good joke in the form of a question. Do not yet give the answer."}
        ]
    )

    print(response.content[0].text)