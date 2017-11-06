import turtle
bob = turtle.Turtle()
bob.width(3)
bob.speed(100)
turtle.colormode(255)
turtle.bgcolor("black")

for times in range(255):
    c = (223,123,221)
    bob.color("blue") 
    bob.circle(225-times)
    bob.right(135)
for times in range(256):
    c = (243,134,234)
    bob.color(c)
    bob.circle(125-times)
    bob.right(135)
for times in range(24):
    c = (255,158,132)
    bob.color("white")
    bob.circle(175-times)
    bob.right(135)
bob = turtle.Turtle()
bob.width(2)
bob.speed(100)
turtle.colormode(255)


