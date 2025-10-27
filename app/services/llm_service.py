import os
import json
from typing import Any, Dict

from anthropic import Anthropic
from dotenv import load_dotenv

from app.models.schemas import GeneratedAssets


def _extract_json(text: str) -> Dict[str, Any]:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start == -1 or end == -1 or end <= start:
            raise ValueError("No JSON object found in LLM response")
        substring = text[start : end + 1]
        return json.loads(substring)


def generate_assets(youtube_url: str, transcript: dict) -> GeneratedAssets:
    """Generate structured assets from a transcript and return a validated GeneratedAssets model."""
    load_dotenv()

    client = Anthropic(api_key=os.environ.get("CLAUDE_API_KEY"))

    prompt = f"""
    You are an expert content strategist. Given the transcript of a YouTube video, return a single valid JSON object (and nothing else) matching the schema described below.

    Schema (keys and types):
    - video_url: string (the original YouTube URL)
    - title_suggestions: array of 3 strings
    - timestamps: array of timestamp strings (format `MM:SS` or `HH:MM:SS`) with brief descriptions, covering key points in the video
    - description: short string (1-3 sentences)
    - hashtags: array of strings (without '#', up to 5 items)
    - linkedin_post: string (1-3 short paragraphs, tailored for LinkedIn)
    - twitter_post: string (one tweet-length string, <= 280 chars)

    Output only a single JSON object. Do not include commentary or markdown. Use the transcript below.

    Transcript:
    ----
{transcript["transcript"]}
----
"""

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )

    raw_text = None
    try:
        raw_text = response.content[0].text
    except Exception:
        raw_text = str(response)

    try:
        parsed = _extract_json(raw_text)
    except Exception as exc:
        raise RuntimeError(f"Failed to parse JSON from LLM response: {exc}\nRaw response: {raw_text}")

    parsed.setdefault("video_url", youtube_url)

    try:
        assets = GeneratedAssets.model_validate(parsed)
    except Exception as exc:
        raise RuntimeError(f"LLM output failed GeneratedAssets validation: {exc}\nParsed JSON: {json.dumps(parsed, indent=2)}\nRaw LLM output: {raw_text}")

    return assets


if __name__ == "__main__":
    load_dotenv()
    if not os.environ.get("CLAUDE_API_KEY"):
        print("CLAUDE_API_KEY not set — set it in your .env or environment to run a live test")
    else:
        example_transcript = "Today we discuss how to design resilient APIs and why input validation matters."
        try:
            assets = generate_assets("https://www.youtube.com/watch?v=example", example_transcript)
            print(assets.json(indent=2))
        except Exception as e:
            print("Error during generate_assets():", e)