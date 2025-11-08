import time
from puzzle_generator import generate_question
from tracker import PerformanceTracker
from adaptive_engine import AdaptiveEngine

def ask_input(prompt):
    try:
        return input(prompt)
    except EOFError:
        return 'End'

def run_game():
    print('=== Math Adaptive Game ===')
    name = ask_input('Enter name: ').strip() or 'Player'
    while True:
        try:
            age = int(ask_input('Enter age (5-10): ').strip())
            if 5 <= age <= 10:
                break
            else:
                print('Age must be between 5 and 10.')
        except ValueError:
            print('Please enter a valid number for age.')
    # Choosing initial difficulty
    start = ask_input('Choose starting difficulty (easy/medium/hard) [default easy]: ').strip().lower()
    if start not in ['easy','medium','hard']:
        start = 'easy'
    engine = AdaptiveEngine(start_level=start)
    tracker = PerformanceTracker()
    print("Type 'End' to finish session anytime.\n")
    while True:
        level = engine.current_level()
        q_text, answer, allow_decimal = generate_question(age, level)
        print(f"Difficulty: {level.capitalize()} | Question: {q_text}")
        t0 = time.time()
        user = ask_input('Your answer: ').strip()
        if user.lower() == 'end':
            break
        t1 = time.time()
        try:
            if allow_decimal:
                user_val = round(float(user), 1)
            else:
                user_val = int(user)
        except:
            print('Invalid answer format; counted as wrong.')
            user_val = None
        correct = (user_val is not None and user_val == answer)
        dt = t1 - t0
        tracker.log(q_text, correct, dt, level)
        old, new, action = engine.update(correct)
        if correct:
            print('✅ Correct!')
        else:
            print(f'❌ Wrong. Correct answer: {answer}')
        if action == 'up':
            print('Level up! Next question will be harder.')
        elif action == 'down':
            print('Level down. Next question will be easier.')
        print('---\n')
    # End of session
    s = tracker.summary()
    print('\n=== Session Summary ===')
    print(f"Player: {name} | Age: {age}")
    print(f"Total Questions: {s['total']}")
    print(f"Correct: {s['correct']}")
    print(f"Accuracy: {s['accuracy']}%") 
    print(f"Average Time per Question: {s['avg_time']}s")
    print(f"Recommended next level: {engine.current_level().capitalize()}")
    print('======================')

if __name__ == '__main__':
    run_game()
