from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

Window.clearcolor=(1,1,1,1)
Window.size=(360,600)
class MainApp(App):
    def build(self):
        layout=BoxLayout(orientation="vertical",spacing=20,padding=50)
        btn=Button(text="Vishwa")
        btn1=Button(text="praveen")
        btn3=Button(text="sarathchandra")
        text=TextInput(text="enter your name : ")
        layout.add_widget(btn)
        layout.add_widget(btn1)
        layout.add_widget(btn3)
        layout.add_widget(text)
        return layout



MainApp().run()