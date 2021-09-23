from kivy import lang
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.layout import Layout

class MainApp(App):
    def build(self):
        layout=GridLayout(cols=2,row_force_default=True,row_default_height=40)
        btn1=Button(text="grade 1",size_hint=(None,None),width=100,height=40)
        btn2=Button(text="grade 2")
        btn3=Button(text="grade 3",size_hint=(None,None),width=100,height=40)
        btn4=Button(text="grade 4")
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        return layout

MainApp().run()        
