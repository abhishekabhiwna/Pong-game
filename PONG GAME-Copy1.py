#!/usr/bin/env python
# coding: utf-8

# # PONG GAME

# In[1]:


import turtle


# In[2]:


wn= turtle.Screen()
wn.title('Pong')


# In[3]:


wn.bgcolor('black')#chaning the background colours of window to black
wn.setup(width=800, height=600)
wn.tracer(0)#it stops window from updating


# In[4]:


#scoew
score_a=0
score_b=0


# In[ ]:





# ## Creating paddles & ball

# In[5]:


#paddle A
paddle_a=turtle.Turtle()#turle object,turtle is module name & Turtule is class name
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)#default size is 20pixel wid and len
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(-350,0)#paddle starting position 


# In[6]:


#paddle b
paddle_b=turtle.Turtle()#turle object,turtle is module name & Turtule is class name
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)#default size is 20pixel wid and len
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350,0)#paddle starting position 


# In[7]:


#Ball

ball=turtle.Turtle()#turle object,turtle is module name & Turtule is class name
ball.speed(0)
ball.shape('square')
ball.color('yellow')
ball.penup()
ball.goto(0,0)#ball starting position 
# Moving BALL
#we need to make ball move in boh directins x and y
ball.dx=0.3
ball.dy=0.3
#it will move ball 2 pixels


# ## Moving paddles

# ## moving paddle a

# In[8]:


def paddle_a_up():
    y=paddle_a.ycor()
    y += 20 #we added 20 pixcels to the y cordinate
    paddle_a.sety(y)#paddle a set y o the new y
    
#keyboard binding
wn.listen() #it tell programm to listen for keyboard inputs
wn.onkeypress(paddle_a_up,"w") #when users press w call the paddle_a_up func


def paddle_a_down():
    y=paddle_a.ycor()
    y -= 20 #we subtract 20 pixcels to the y cordinate
    paddle_a.sety(y)#paddleb set y to the new y
    
#keyboard binding
wn.listen() #it tell programm to listen for keyboard inputs
wn.onkeypress(paddle_a_down,"s") #when users press s call the paddle_a_up func


# ## moving paddle b

# In[9]:


def paddle_b_up():
    y=paddle_b.ycor()
    y += 20 
    paddle_b.sety(y)
    
#keyboard binding
wn.listen() 
wn.onkeypress(paddle_b_up,"p") 


def paddle_b_down():
    y=paddle_b.ycor()
    y -= 20 
    paddle_b.sety(y)
    
#keyboard binding
wn.listen() 
wn.onkeypress(paddle_b_down,"l") 


# ## Scoring system

# In[10]:


#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0 Player B:0", align="center",font=("Courier",24,"normal"))


# In[11]:


#Main Game Loop
while True:
    wn.update()# everytime loops run it update the screen
    
      #move the ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)
    
    #Border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*= -1 #reverse the diection of ball, when ball hits the top border
        
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*= -1 #reverse the diection of ball, when ball hits the bottom border
        
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*= -1 #reverse the diection of ball, when ball hits the right border
        score_a +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center",font=("Courier",24,"normal"))
        
    if ball.xcor()<-390:
        ball.goto(-0,0)
        ball.dx*= -1 #reverse the diection of ball, when ball hits the left border
        score_b +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center",font=("Courier",24,"normal"))
        


        
    #bounce
    if (ball.xcor()>340 and ball.xcor() <350) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()> paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx *= -1
        
    if (ball.xcor()<-340 and ball.xcor() >-350) and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()> paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1



    
  
    
    

