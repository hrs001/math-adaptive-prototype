import time
from typing import List, Dict

class PerformanceTracker:
    def __init__(self):
        self.records: List[Dict] = []

    def log(self, question_text, correct: bool, time_taken: float, difficulty: str):
        self.records.append({
            'question': question_text,
            'correct': bool(correct),
            'time': float(time_taken),
            'difficulty': difficulty
        })

    def summary(self):
        total = len(self.records)
        if total == 0:
            return {'total':0, 'correct':0, 'accuracy':0.0, 'avg_time':0.0}
        correct = sum(1 for r in self.records if r['correct'])
        avg_time = sum(r['time'] for r in self.records) / total
        acc = (correct / total) * 100.0
        return {
            'total': total,
            'correct': correct,
            'accuracy': round(acc, 2),
            'avg_time': round(avg_time, 2)
        }
