
# utils/helpers.py
def calculate_progress(completed: int, total: int) -> float:
    if total == 0:
        return 0.0
    return round((completed / total) * 100, 2)

def validate_audio_format(filename: str) -> bool:
    return filename.lower().endswith(('.mp3', '.wav', '.m4a'))
