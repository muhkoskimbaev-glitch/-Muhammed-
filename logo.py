def draw_logo():
    

    try:
        import turtle

        screen = turtle.Screen()
        screen.title("Мой логотип — Kenzhebek Muhammed")
        screen.bgcolor("black")
        screen.setup(width=600, height=600)
        screen.tracer(0)  

        t = turtle.Turtle()
        t.hideturtle()

        
        RADIUS = 160
        t.penup()
        t.goto(0, -RADIUS)
        t.pendown()
        t.pencolor("white")
        t.pensize(8)
        t.setheading(0)

        for _ in range(360):
            t.forward(2 * 3.14159 * RADIUS / 360)
            t.left(1)

        
        t.penup()
        t.goto(0, -60)
        t.pendown()
        t.pencolor("#1E90FF")
        t.write("МК", align="center", font=("Courier", 80, "bold"))

    
        t.penup()
        t.goto(0, -RADIUS - 45)
        t.pendown()
        t.pencolor("white")
        t.write("KENZHEBEK MUHAMMED", align="center", font=("Courier", 15, "bold"))

        screen.update()
        screen.mainloop()

    except Exception as e:
        print(f"  ⚠️  Turtle недоступен: {e}")
        print("  Запусти программу в среде с графическим интерфейсом.")
