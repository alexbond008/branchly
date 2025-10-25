import json
from pathlib import Path

class FilestorageService:
    def __init__(self, basepath = "data"):
        self.basepath = Path(basepath)

    def save_json(self, subdir: str, filename: str, data: dict) -> str:
        path = self.basepath / subdir / f"{filename}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)

        return str(path)
    
    def read_json(self, subdir: str, filename: str) -> dict:
        path = self.basepath / subdir / f"{filename}.json"
        with open(path, 'r') as f:
            data = json.load(f)

        return data
    

if __name__ == "__main__":
    storage = FilestorageService()
    test_data = {"key": "value", "number": 43}
    saved_path = storage.save_json("test_dir", "test_file", test_data)
    print(f"Data saved to: {saved_path}")

    loaded_data = storage.read_json("test_dir", "test_file")
    print(f"Data loaded: {loaded_data}")