import turtle

tortuga = turtle.Turtle()
bob = turtle.Turtle()
calvin = turtle.Turtle()


def customize_turtle(turtle, color, shape, speed):
    turtle.shape(shape)
    turtle.color(color)
    turtle.speed(speed)


def make_a_square(turtle):
    for i in range(0, 4):
        turtle.forward(125)
        turtle.right(90)


customize_turtle(tortuga, 'blue', 'square', 3)
customize_turtle(bob, 'green', 'arrow', 2)
customize_turtle(calvin, 'red', 'turtle', 9)

my_window = turtle.Screen()
my_window.bgcolor('white')
make_a_square(tortuga)
calvin.circle(100)
bob.forward(20)
bob.circle(15)

my_window.exitonclick()
