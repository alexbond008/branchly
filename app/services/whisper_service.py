import whisper

def transcribe_audio(audio_info: dict) -> dict:
    file_path = audio_info["file_path"]
    video_id = audio_info["video_id"]
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return {"transcript": result["text"], "video_id": video_id}

if __name__ == "__main__":
    sample_file = "data/uploads/5a98fbe5-7b29-4fad-8602-2084c566f441.mp3"
    transcription = transcribe_audio({"file_path": sample_file, "video_id": "sample"})
    print("Transcription:", transcription)