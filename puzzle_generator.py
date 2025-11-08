import random

def generate_question(age: int, difficulty: str):
    difficulty = difficulty.lower()

    if 5 <= age <= 7:
        if difficulty == 'easy':
            a, b = random.randint(0, 10), random.randint(0, 10)
            return f"{a} + {b} = ?", a + b, False
        elif difficulty == 'medium':
            a, b = random.randint(0, 10), random.randint(0, 10)
            return f"{a} x {b} = ?", a * b, False
        else:
            op = random.choice(['-', '/'])
            if op == '-':
                a, b = random.randint(0, 20), random.randint(0, 20)
                if b > a: a, b = b, a
                return f"{a} - {b} = ?", a - b, False
            else:
                b = random.randint(1, 10)
                c = random.randint(0, 10)
                a = b * c
                return f"{a} ÷ {b} = ?", c, False

    elif 8 <= age <= 10:
        if difficulty == 'easy':
            expr = f"{random.randint(1, 30)} + {random.randint(1, 20)} - {random.randint(1, 10)}"
        elif difficulty == 'medium':
            expr = f"{random.randint(1, 20)} + {random.randint(1, 10)} x {random.randint(1, 10)} - {random.randint(1, 5)}"
        else:
            expr = f"{random.randint(10, 50)} ÷ {random.randint(1, 10)} + {random.randint(1, 10)} x {random.randint(1, 5)} - {random.randint(1, 5)}"
        ans = eval(expr.replace('x', '*').replace('÷', '/'))
        if difficulty == 'hard':
            ans = round(ans, 1)
            return expr + " = ? (round to 1 decimal)", ans, True
        else:
            return expr + " = ?", int(ans), False

    else:
        raise ValueError("Age must be between 5 and 10.")
