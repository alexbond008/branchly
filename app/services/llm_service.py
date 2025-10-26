import os 
from anthropic import Anthropic
from dotenv import load_dotenv


def generate_assets(transcript :str) -> str:
    
    load_dotenv() 

    client = Anthropic(
        api_key=os.environ.get("CLAUDE_API_KEY")
    )

    prompt = f"""
    You are a expert content strategist. Given the transcript of the youtube video:
    ----
    {transcript}
    ----
    Generate:
    1. 3 YouTube title suggestions
    2. 3 timestamps of interesting moments
    3. A LinkedIn post
    4. A Twitter post

    Provide the response in the following JSON format:
    {{
        "title_suggestions": [list of 3 youtube worthy titles],
        "timestamps": [list of timestamps],
        "linkedin_post": "string",
        "twitter_post": "string"
    }}

    When generating titles, make them catchy and engaging.
    For timestamps, pick moments that would intrigue viewers to watch the video.
    Ensure the LinkedIn and Twitter posts are tailored to their respective audiences and platforms.
    """
    reponse = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=2000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return reponse.content[0].text



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