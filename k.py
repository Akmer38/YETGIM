import turtle

# Turtle ayarları
t = turtle.Turtle()
t.speed(3)
t.color('red')
t.fillcolor('pink')

# Kalp çizimi
def draw_heart():
    t.begin_fill()
    t.left(140)
    t.forward(180)
    
    # Sol yarım daire
    for _ in range(200):
        t.right(1)
        t.forward(1)
    
    t.left(120)
    
    # Sağ yarım daire
    for _ in range(200):
        t.right(1)
        t.forward(1)
    
    t.forward(180)
    t.end_fill()

# Başlangıç pozisyonu
t.penup()
t.goto(0, -100)
t.pendown()

# Kalbi çiz
draw_heart()

# "Seni Seviyorum" yazısı
t.penup()
t.goto(0, -200)
t.pendown()
t.color('red')
t.write('♥', align='center', font=('Arial', 30, 'bold'))

# Pencereyi açık tut
t.hideturtle()
turtle.done()