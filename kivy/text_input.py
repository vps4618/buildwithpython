from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout

class MainApp(App):

    def build(self):
        
        layout=GridLayout(cols=2,row_force_default=True,row_default_height=40,spacing=20,padding=30)
        self.weight=TextInput(text="")
        self.height=TextInput(text="")
        label1=Label(text="Enter weight"+"\n"+"in below button.")
        label2=Label(text="Enter height"+"\n"+"in below button.")
        submit=Button(text="submit",on_press=self.submit )

        layout.add_widget(label1)
        layout.add_widget(label2)
        layout.add_widget(self.weight)
        layout.add_widget(self.height)
        layout.add_widget(submit)
        
        return layout


    def submit(self,obj):

        print("weight : "+self.weight.text)
        print("height : "+self.height.text)    
        print("\n")

MainApp().run()        