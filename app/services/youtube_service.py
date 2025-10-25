import yt_dlp
from pathlib import Path
import uuid

def download_audio(youtube_url: str, output_dir = "data/uploads") -> dict:
    """
    Downloads audio from a Youtube video URL and saves it to the specified output directory.

    Args:
        youtube_url (str): The URL of the Youtube video.
        output_dir (str): The directory where the audio file will be saved.
    Returns:
        dict: A dictionary containing the file path and the video id.
    
    """

    video_id = str(uuid.uuid4())
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    base_path = str(output_path / f"{video_id}")
    final_mp3 = base_path + ".mp3"

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': base_path + '.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    
    return {"file_path": final_mp3, "video_id": video_id}


if __name__ == "__main__":
    test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    result = download_audio(test_url)
    print(f"Audio downloaded to: {result['file_path']} with video ID: {result['video_id']}")