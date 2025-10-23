"""
PROJECT CONTEXT — "Branchly" (working title)
------------------------------------------
Goal:
Build a backend system (in Python using FastAPI) for a creator tool that transforms long-form YouTube videos into multi-platform content assets.

Core idea:
A YouTube video acts as the ROOT NODE. From it, we extract intelligence and generate derivative assets:
- Transcripts
- Timestamps
- Blog posts
- LinkedIn posts
- Tweets
- Video titles and descriptions

Later, the system will expand to include:
- AI short-form clip generation (Vizard-style)
- Automatic scheduling & posting to TikTok, YouTube Shorts, LinkedIn, X

----------------------------------------------------------
🔧 TECHNICAL STACK
----------------------------------------------------------
Backend Framework:
- Python 3.11+
- FastAPI (primary API framework)
- Async support with uvicorn

AI Tools:
- OpenAI Whisper API (for transcription)
- OpenAI GPT-4 / GPT-5 API (for LLM text generation)
- (Optional) LangChain for prompt management

Database:
- Supabase (PostgreSQL)
- Tables:
    - users (id, email, auth_id)
    - videos (id, user_id, title, url, transcript_text, created_at)
    - generated_assets (id, video_id, asset_type, content, created_at)

Storage:
- Supabase Storage for uploaded videos & transcription files

----------------------------------------------------------
🧩 INITIAL MVP ENDPOINTS
----------------------------------------------------------

1. POST /upload_video
   - Input: YouTube URL or uploaded MP4 file
   - Task: Download (using yt-dlp if URL), extract audio, store in Supabase
   - Output: video_id, status

2. POST /transcribe/{video_id}
   - Input: video_id
   - Task: Send audio to Whisper API, save transcript to DB
   - Output: transcript_text, status

3. POST /generate_assets/{video_id}
   - Input: video_id, (optional) content_type=["tweets", "linkedin", "titles"]
   - Task: Fetch transcript → Send to GPT → Generate JSON of assets
   - Output: JSON with generated assets (title ideas, tweets, LinkedIn post, timestamps, etc.)

4. GET /assets/{video_id}
   - Input: video_id
   - Output: All generated assets related to that video

5. GET /health
   - Simple heartbeat check for the API

----------------------------------------------------------
🧠 LLM PROMPTING LOGIC
----------------------------------------------------------
LLM receives a system prompt like:
"You are an AI that helps creators repurpose long-form video content into optimized short-form text for various platforms."

Given transcript text → generate:
- 3 engaging video title ideas
- 1 YouTube description rewrite
- 3 tweets or X posts optimized for virality
- 1 LinkedIn post (professional tone)
- Key timestamps for video moments (based on topic or tone shifts)

Responses stored in JSON format like:
{
  "titles": [...],
  "youtube_description": "...",
  "tweets": [...],
  "linkedin_post": "...",
  "timestamps": [{"time": "00:02:14", "topic": "Intro to airflow simulation"}]
}

----------------------------------------------------------
💾 FOLDER STRUCTURE (RECOMMENDED)
----------------------------------------------------------
/backend
│
├── main.py                # FastAPI entry point
├── config.py              # Environment variables & API keys
├── database.py            # Supabase connection
├── models.py              # SQLAlchemy or Pydantic models
├── routes/
│   ├── upload.py
│   ├── transcribe.py
│   ├── generate.py
│   └── assets.py
│
├── services/
│   ├── youtube_downloader.py  # yt-dlp integration
│   ├── transcription.py       # Whisper API logic
│   ├── llm_generation.py      # GPT prompt construction
│   └── storage.py             # Supabase upload/download logic
│
├── utils/
│   ├── logging.py
│   ├── validation.py
│   └── helpers.py
│
└── requirements.txt

----------------------------------------------------------
🌍 DESIGN PRINCIPLES
----------------------------------------------------------
- Keep everything async (async def, await)
- Use Pydantic models for input/output validation
- Modular architecture: services handle logic, routes handle HTTP
- Error handling with custom HTTPException
- Configs & secrets pulled from environment variables (.env)
- Logging every request + external API call

----------------------------------------------------------
✅ NEXT DEVELOPMENT STEPS
----------------------------------------------------------
1. Implement FastAPI project skeleton + base routes
2. Add /upload_video route with YouTube URL and file upload support
3. Integrate Whisper API for transcription
4. Build /generate_assets route using OpenAI GPT-4
5. Store and retrieve results from Supabase
6. Test with Postman / frontend prototype

----------------------------------------------------------
💡 Example Vision
----------------------------------------------------------
One day, a creator uploads a YouTube video URL, and this system:
1. Downloads and transcribes the video.
2. Extracts timestamps and topic structure.
3. Feeds this into an AI model to generate:
   - Tweets
   - LinkedIn posts
   - Blog article summary
   - Optimized title ideas
4. Stores everything under that video ID.
5. Frontend UI later allows scheduling posts across platforms.

This file is meant to help GitHub Copilot understand:
- The architecture
- The purpose of each module
- The long-term vision (so it can propose coherent functions)

"""

