import turtle
pen = turtle.Turtle()
pen.shape("arrow")
pen.speed(5)

window = turtle.Screen()
window.bgcolor("black")

#Draw the frame for the flag
pen.color("white")
pen.pensize(2)
pen.fillcolor("white")

pen.penup()
pen.goto(-180, -120)
pen.pendown()
pen.begin_fill()
pen.goto(180,-120)
pen.goto(180,120)
pen.goto(-180,120)
pen.goto(-180, -120)
pen.end_fill()  
  
#Draw the red vertical stripe
pen.color("red")
pen.pensize(2)
pen.fillcolor("red")

pen.penup()
pen.goto(-180, -120)
pen.pendown()
pen.begin_fill()
pen.goto(-60,-120)
pen.goto(-60,120)
pen.goto(-180,120)
pen.goto(-180, -120)
pen.end_fill()  
#Draw the red horizontal stripe
pen.color("red")
pen.pensize(2)
pen.fillcolor("red")

pen.penup()
pen.goto(-60, 40)
pen.pendown()
pen.begin_fill()
pen.goto(180,40)
pen.goto(180,-40)
pen.goto(-60,-40)
pen.goto(-60, 40)
pen.end_fill() 
#Draw the green horizontal stripe
pen.color("green")
pen.pensize(2)
pen.fillcolor("green")

pen.penup()
pen.goto(-60, -40)
pen.pendown()
pen.begin_fill()
pen.goto(180,-40)
pen.goto(180,-120)
pen.goto(-60,-120)
pen.goto(-60, -40)
pen.end_fill() 


#Draw the khanjar shape by shape

pen.color("#F5F5F5")
pen.pensize(2)
pen.fillcolor("#F5F5F5")

pen.penup()
pen.goto(-160, 100)
pen.pendown()
pen.begin_fill()
pen.goto(-160, 105)
pen.goto(-80, 50)
pen.goto(-80, 45)
pen.goto(-160, 100)
pen.end_fill() 


pen.penup()
pen.goto(-160, 50)
pen.pendown()
pen.begin_fill()
pen.goto(-160, 45)
pen.goto(-80, 100)
pen.goto(-80, 105)
pen.goto(-160, 50)
pen.end_fill() 


pen.penup()
pen.goto(-125, 102)
pen.pendown()
pen.begin_fill()
pen.goto(-125, 112)
pen.goto(-115, 112)
pen.goto(-115, 102)
pen.goto(-125, 102)
pen.end_fill() 


pen.penup()
pen.goto(-122, 95)
pen.pendown()
pen.begin_fill()
pen.goto(-122, 102)
pen.goto(-118, 102)
pen.goto(-118, 95)
pen.goto(-122, 95)
pen.end_fill() 


pen.penup()
pen.goto(-125, 63)
pen.pendown()
pen.begin_fill()
pen.goto(-125, 95)
pen.goto(-115, 95)
pen.goto(-115, 63)
pen.goto(-125, 63)
pen.end_fill() 


pen.penup()
pen.goto(-125, 63)
pen.pendown()
pen.begin_fill()
pen.goto(-125, 73)
pen.goto(-140, 73)
pen.goto(-125, 63)
pen.end_fill() 


pen.penup()
pen.goto(-125, 77)
pen.pendown()
pen.begin_fill()
pen.goto(-135, 79)
pen.goto(-135, 81)
pen.goto(-125, 81)
pen.goto(-125, 79)
pen.end_fill() 


pen.penup()
pen.goto(-135, 77)
pen.pendown()
pen.begin_fill()
pen.goto(-150, 77)
pen.goto(-150, 83)
pen.goto(-135, 83)
pen.goto(-135, 77)
pen.end_fill() 


pen.penup()
pen.goto(-115, 79)
pen.pendown()
pen.begin_fill()
pen.goto(-105, 79)
pen.goto(-105, 81)
pen.goto(-115, 81)
pen.goto(-115, 79)
pen.end_fill() 


pen.penup()
pen.goto(-105, 77)
pen.pendown()
pen.begin_fill()
pen.goto(-90, 77)
pen.goto(-90, 83)
pen.goto(-105, 83)
pen.goto(-105, 77)
pen.end_fill() 




pen.penup()
pen.goto(-140, -160)
pen.color("white")
pen.write("Happy 54th National Day", None, None, "20pt bold")


pen.hideturtle()


