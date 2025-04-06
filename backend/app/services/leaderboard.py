# app/services/leaderboard.py
from typing import List

def get_global_leaderboard() -> List[dict]:
    # Simula recuperação de ranking global
    return [
        {"name": "Dylan", "country": "USA", "score": 2400},
        {"name": "Miles", "country": "Germany", "score": 1800},
    ]
