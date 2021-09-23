# step 1-create the app
# step 2-create the game
# step 3-build the game
# step 4-run the app
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty,ReferenceListProperty,ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

Window.clearcolor=(118/255.0,149/255.0,192/255.0,1)

#touch events
 
# on_touch_down() - when our fingers/mouse touches the screen
# on_touch_up() - when we lift our fingers off the screen after touching it
# on_touch_move() - when we drag our fingers on the screen


class PongPaddle(Widget):
    score=NumericProperty(0)
    def bounce_ball(self,ball):#collision detection
        if self.collide_widget(ball):
            ball.velocity_x *= -1

class PongBall(Widget):
    velocity_x=NumericProperty(0) #set its data type to integer
    velocity_y=NumericProperty(0)
    velocity=ReferenceListProperty(velocity_x,velocity_y)

    # latest position = current velocity + current position
    def move(self):
        self.pos=Vector(*self.velocity)+self.pos

#update - moving ball by calling move() and other stuff
class PongGame(Widget):
    ball=ObjectProperty( None)
    player1=ObjectProperty(None)
    player2=ObjectProperty(None)

    def serve_ball(self):
        self.ball.velocity=Vector(7,0).rotate(randint(0,360))
    def update(self,dt):
        self.ball.move()   
        

        # bounce off top and bottom
        if (self.ball.y<0) or (self.ball.y>self.height-50):
            self.ball.velocity_y *= -1

        # bounce off left and increase the score
        if self.ball.x<0:
            self.ball.velocity_x *= -1
            self.player1.score+=1

        #bounce off right    
        if self.ball.x>self.width-50:
            self.ball.velocity_x *= -1
            self.player2.score+=1

        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)    
    
    def on_touch_move(self, touch):
        if touch.x < self.width/1/4:
            self.player1.center_y=touch.y
        if touch.x > self.width*3/4:
            self.player2.center_y=touch.y                




class PongApp(App):
    def build(self): #method name as build is important
        game=PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update,1.0/60.0)  # in one second 60 freames are shown
        return game
        
        

PongApp().run()

#in  kv file its name should be  first name of the class.(Pong)
# we can use tab button for get some space