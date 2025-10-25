import whisper

def transcribe_audio(file_path: str) -> str:
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result["text"]

if __name__ == "__main__":
    sample_file = "data/uploads/5a98fbe5-7b29-4fad-8602-2084c566f441.mp3"
    transcription = transcribe_audio(sample_file)
    print("Transcription:", transcription)