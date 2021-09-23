from kivy.app import App
from kivy.uix.behaviors import button
from kivy.uix.button import Button
from kivy.uix.image import Image,AsyncImage
from kivy.uix.widget import Widget

class MainApp(App):
    def build(self):
        button=Button(text="hi",font_size="40px",
        size_hint=(0.2,0.2),
        pos_hint={'center_x':0.1,'center_y':0.5
        },on_press=self.printpress,on_release=self.printrelease)
            

        # img=Image(source="icon.png")
        img=AsyncImage(source="https://iconarchive.com/download/i78115/igh0zt/ios7-style-metro-ui/MetroUI-Apps-Paint.ico")
        rootwindow=Widget()
        
        rootwindow.add_widget(button)
        return img




    def printpress(self,obj):
        print("button has been pressed")
    def printrelease(self,obj1):
        print("button has been released")


MainApp().run()        