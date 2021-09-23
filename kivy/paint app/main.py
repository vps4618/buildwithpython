
import random

from kivy.app import App
from kivy.core import text
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Ellipse,Color,Line
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

# RGBA - red,green,blue,opacity
# Window.clearcolor=(1,0,0,0)

#how get more background colours

# Window.clearcolor=(127/255.0,129/255.0,195/255.0,1)

Window.clearcolor=(1,1,1,1)



class PaintWindow(Widget):

    def on_touch_down(self, touch):
        colorR=random.randint(0,255)
        colorG=random.randint(0,255)
        colorB=random.randint(0,255)
        self.canvas.add(Color(rgb=(colorR/255.0,colorG/255.0,colorB/255.0)))
        d=30
        self.canvas.add(Ellipse(pos=(touch.x-d/2,touch.y-d/2),size=(d,d)))
        # ud refers to a dictionary in kivy
        touch.ud['line']=Line(points=(touch.x,touch.y)) #line is the name of the touch dictionary
        self.canvas.add(touch.ud['line'])
    def on_touch_move(self, touch):
        touch.ud['line'].points+=[touch.x,touch.y] 
       

# root window = Paint window + button           
class PaintApp(App,Widget):
    def build(self):
        layout=GridLayout(cols=1,row_force_default=True,row_default_height=50,spacing=20,padding=30)
        
       
        self.painter=PaintWindow()
        clearbtn=Button(text="Clear",font_size="15sp",size_hint=(None,None),width=150,height=50)
        black=Button(text="black",font_size="15sp",size_hint=(None,None),width=150,height=50)
        white=Button(text="white",font_size="15sp",size_hint=(None,None),width=150,height=50)
        random=Button(text="random",font_size="15sp",size_hint=(None,None),width=150,height=50)
        clearbtn.bind(on_release=self.clear_canvas)
        black.bind(on_release=self.changeblack)
        white.bind(on_release=self.changewhite)
        random.bind(on_release=self.changerandom)
        label=Label(text="Vishwa Praveen's"+"\n"+"First Simple Paint App",font_size="15sp",color=(45/255.0,158/255.0,235/255.0,1),bold=True,italic=True,size_hint=(None,None),width=250,height=30)
        layout.add_widget(label)  
       
        layout.add_widget(clearbtn)
        layout.add_widget(black)
        layout.add_widget(white)
        layout.add_widget(random)
      
        layout.add_widget(self.painter)
    
    
        return layout

        
    def clear_canvas(self,obj):
        self.painter.canvas.clear()
    def changeblack(self,obj):
        self.painter.canvas.clear()
        Window.clearcolor=(0,0,0,0)    
    def changewhite(self,obj):
        self.painter.canvas.clear()
        Window.clearcolor=(1,1,1,1)

    def changerandom(self,obj):
        self.painter.canvas.clear()
        colorR=random.randint(0,255)
        colorG=random.randint(0,255)
        colorB=random.randint(0,255)
        Window.clearcolor=(colorR/255.0,colorG/255.0,colorB/255.0,1)
        
                   



        
            



PaintApp().run()


# 1.CHANGING BACKGROUND COLOURS AND RGB COLOURS
# 2.ON_TOUCH_DOWN
# 3.COLOUR
# 4.DRAWING CIRCLES/ELIIPSE


# steps of creating a brush

#1.import Line graphics
#2.create a touch dictionary ->Store the initial point in it
#3.When the mouse is dragged to extend the line store the next points inside 
#4.Store it inside canvas
#5.Random colours
