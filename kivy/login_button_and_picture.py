from kivy.app import App
from kivy.core.window import Window
from kivy.uix.behaviors import button
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

Window.clearcolor=(1,1,1,1)
Window.size=(360,600)
class MainApp(App):
    def build(self):
        layout=BoxLayout(orientation="vertical",spacing=100,padding=200)
        image=Image(source="icon.png",size_hint=(None,None),width=200,height=100,pos_hint={'center_x':0.5})
        button=Button(text="Login",size_hint=(None,None),pos_hint={'center_x':0.5},width=100,height=50)
        layout.add_widget(image)
        layout.add_widget(button)
        return layout



MainApp().run()