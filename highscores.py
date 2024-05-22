# highscores.py

import os

SCORE_FILE = "highscores.txt"

def load_high_scores():
    if not os.path.exists(SCORE_FILE):
        return []
    
    with open(SCORE_FILE, 'r') as file:
        scores = [int(line.strip()) for line in file.readlines()]
    
    return scores

def save_high_score(new_score):
    scores = load_high_scores()
    scores.append(new_score)
    scores = sorted(scores, reverse=True)[:5]  # Keep top 5 scores

    with open(SCORE_FILE, 'w') as file:
        for score in scores:
            file.write(f"{score}\n")

    return scores
