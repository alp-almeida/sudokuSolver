
import turtle as te

t= te.Turtle()
s= te.Screen()

s.bgcolor('black')
t.pencolor('green')
t.speed(0)

col = ['white','blue','yellow','green']

c=0

for i in range(500):
    t.forward(i*10)
    t.right(144)
    t.color(col[c])
    if c==3:
        c=0
    else:
        c+=1
