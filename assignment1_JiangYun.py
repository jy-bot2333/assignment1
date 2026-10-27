# Name: [Jiang Yun]
# Assignment One

import turtle

# ---------------- Setup ----------------
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Shapes with Turtle")

t = turtle.Turtle()
t.speed(0)          # fastest drawing
t.pensize(3)

COLORS = ["red", "orange", "yellow", "green", "cyan", "blue", "magenta"]


# ---------------- Helper ----------------
def move_to(x, y, heading=0):

    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()


# ---------------- 1. Square ----------------
def draw_square(size):
    for i in range(4):               # structured for loop
        t.color(COLORS[i])           # color changes each side
        t.forward(size)
        t.left(90)


# ---------------- 2. Triangle ----------------
def draw_triangle(size):
    for i in range(3):
        t.color(COLORS[i + 3])
        t.forward(size)
        t.left(120)


# ---------------- 3. Star ----------------
def draw_star(size):
    for i in range(5):
        t.color(COLORS[i])
        t.forward(size)
        t.right(144)                 # 144 degrees makes a 5-point star


# ---------------- 4. Colorful pattern (dynamic color & length) ----------------
def draw_rainbow_spiral(turns=36):
    for i in range(turns):
        t.color(COLORS[i % len(COLORS)])   # dynamic color
        t.pensize(1 + i % 6)               # dynamic pen size
        side = 20 + i * 4                  # dynamic length (grows each loop)
        for _ in range(4):                 # draw one square
            t.forward(side)
            t.left(90)
        t.left(10)


# ---------------- Main drawing ----------------
move_to(-300, 150)
draw_square(100)

move_to(-300, -80)
draw_triangle(110)

move_to(80, 160)
draw_star(110)

move_to(80, -180)
draw_rainbow_spiral(36)

t.hideturtle()
screen.exitonclick()   # click the window to close



#==========================================
#----------------QA Bot-------------------
print("=" * 50)
print("   HKU QA Bot   (type 'bye' to exit)")
print("=" * 50)
print("Ask me about: HKU, robot, jetson, ai, human")

while True:                                   # keep the conversation going
    question = input("\nYou: ").strip().lower()   # .lower() -> case-insensitive

    # ---- 1. empty input ----
    if question == "":
        print("Bot: Please type something. :)")
        continue

    # ---- 2. exit commands ----
    elif question in ("bye", "exit", "quit", "goodbye"):
        print("Bot: Goodbye! See you at HKU.")
        break

    # ---- 3. keyword matching: HKU ----
    elif "hku" in question:
        print("Bot: HKU is The University of Hong Kong, "
              "founded in 1911 and the oldest tertiary institution in Hong Kong.")

    # ---- 4. keyword: robot ----
    elif "robot" in question:
        print("Bot: A robot is a programmable machine that senses its "
              "environment and acts on it. Many HKU projects use robots.")

    # ---- 5. keyword: jetson ----
    elif "jetson" in question:
        print("Bot: NVIDIA Jetson is a small, low-power AI computer used for "
              "edge computing - great for robots, drones and cameras.")

    # ---- 6. keyword: ai ----
    elif "ai" in question or "artificial intelligence" in question:
        print("Bot: AI (Artificial Intelligence) is the science of making "
              "machines perform tasks that normally need human intelligence.")

    # ---- 7. keyword: human ----
    elif "human" in question:
        print("Bot: Humans are the ones who design, train and use AI systems. "
              "Human-in-the-loop is important for safety and ethics.")

    # ---- 8. fallback ----
    else:
        print("Bot: Sorry, I don't understand that yet. "
              "Try asking about HKU, robot, jetson, ai or human.")



#========================================
#====================================simple calculator
def get_number(prompt):
    """Keep asking until the user types a valid number."""
    while True:
        text = input(prompt).strip()
        try:
            return float(text)          # works for "3", "-2.5", "10"
        except ValueError:
            print("  ! That's not a number. Please try again.")


def get_operator():
    """Keep asking until the user enters one of + - * /"""
    while True:
        op = input("Choose operator (+, -, *, /): ").strip()
        if op in ("+", "-", "*", "/"):
            return op
        print("  ! Invalid operator. Please enter +, -, * or /.")


def calculate(a, op, b):
    """Do the math and return the result (or an error message)."""
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    else:  # op == "/"
        if b == 0:
            return "Error: cannot divide by zero"
        return a / b


def main():
    print("=" * 40)
    print("      Simple Calculator")
    print("=" * 40)

    while True:
        # 1. first number
        num1 = get_number("First number : ")
        # 2. operator
        op = get_operator()
        # 3. second number
        num2 = get_number("Second number: ")

        # 4. compute and display
        result = calculate(num1, op, num2)
        print("-" * 40)
        if isinstance(result, str):          # error message
            print(result)
        else:
            print(f"{num1:g} {op} {num2:g} = {result:g}")
        print("-" * 40)

        # 5. again?
        again = input("Calculate again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
