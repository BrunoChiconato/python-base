from turtle import Turtle

print(
"""\
Turtle Game

CLI Commands:
    move x y
    move steps
    turn angle (default 90)
    draw shape size (line | circle)
    write text
    stop | exit
"""
)

turtle = Turtle()
turtle.shape("turtle")
turtle.speed(3)
turtle.color("blue", "yellow")
turtle.shapesize(2, 2, 2)
turtle.penup()

while True:
    command: list[str] = input("Turtle: ").strip().split()

    match command:
        case ["move", *points]:
            match points:
                case [x, y]:
                    turtle.goto(float(x), float(y))
                case [steps]:
                    turtle.forward(float(steps))
        case ["turn", *options]:
            match options:
                case [angle]:
                    turtle.right(float(angle))
                case _:
                    turtle.right(90)
        case ["draw", shape, size]:
            turtle.pendown()
            match shape:
                case "line":
                    turtle.forward(float(size))
                case "circle":
                    turtle.circle(float(size))
            turtle.penup()
        case ["write", text]:
            turtle.write(" ".join(text), None, "center", "16pt 20")
        case ["exit" | "stop" | "quit"]:
            break
        case _:
            print("Invalid command")