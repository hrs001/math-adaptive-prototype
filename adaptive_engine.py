# Implements the rule-based adaptive engine described.
class AdaptiveEngine:
    levels = ['easy', 'medium', 'hard']

    def __init__(self, start_level='easy'):
        if start_level not in self.levels:
            raise ValueError('Invalid start level')
        self.current_index = self.levels.index(start_level)
        self.consecutive_correct = 0
        self.consecutive_wrong = 0

    def current_level(self):
        return self.levels[self.current_index]

    def update(self, correct: bool):
        """Update engine state given if latest answer was correct.
        Return a tuple (old_level, new_level, action) where action in {'stay','up','down'}.
        """
        old = self.current_level()
        action = 'stay'
        if correct:
            self.consecutive_correct += 1
            self.consecutive_wrong = 0
        else:
            self.consecutive_wrong += 1
            self.consecutive_correct = 0

        # Level up rule: easy->medium needs 3 correct in row, medium->hard needs 5 correct in row
        if self.current_index == 0 and self.consecutive_correct >= 3:
            self.current_index = 1
            self.consecutive_correct = 0
            action = 'up'
        elif self.current_index == 1 and self.consecutive_correct >= 5:
            self.current_index = 2
            self.consecutive_correct = 0
            action = 'up'
        # Level down rule: any level down on 2 consecutive wrong answers
        elif self.consecutive_wrong >= 2 and self.current_index > 0:
            self.current_index -= 1
            self.consecutive_wrong = 0
            action = 'down'

        new = self.current_level()
        return old, new, action
