import turtle

t = turtle.Pen()

my_colors = ("red","green","yellow","black")

t.width(5)
t.speed(10)

for i in range(10):        #0,1,
    t.penup()
    t.goto(0,-i*10)      #0,-100,-200
    t.pendown()
    t.color(my_colors[i%len(my_colors)])
    t.circle(10+i*10)   #100,200,300

# t.goto(0,-100)
# t.circle(200)
#
# t.goto(0,-200)
# t.circle(300)


turtle.done()   #程序结束后，窗口依然在