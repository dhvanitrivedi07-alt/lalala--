import math
from turtle import *

# ---------------- HEART MATH ----------------
def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return (13 * math.cos(k)
            - 5 * math.cos(2*k)
            - 2 * math.cos(3*k)
            - math.cos(4*k))

# ---------------- SCREEN SETUP ----------------
screen = Screen()
screen.bgcolor("black")
screen.title("F1 HEART MODE")
tracer(False)          # force manual refresh

color("#e10600")       # F1 red
pensize(2)
speed(0)

# ---------------- DRAW HEART ----------------
penup()
goto(0, 0)
pendown()

for i in range(6000):
    k = math.radians(i)
    goto(hearta(k) * 20, heartb(k) * 20)

# ---------------- STOP DRAWING ----------------
penup()
hideturtle()

# ---------------- WRITE TEXT (CENTER) ----------------
goto(0, -20)
color("white")
write(
    "CAN WE PLEASE TALK??\nJUST FOR ONCE...",
    align="center",
    font=("Arial", 16, "bold")
)

# ---------------- F1 TEXT ----------------
goto(0, -120)
color("#e10600")
write(
    "F1 MODE 🏎️",
    align="center",
    font=("Arial", 18, "bold")
)

# ---------------- UPDATE SCREEN ----------------
update()        # VERY IMPORTANT
done()