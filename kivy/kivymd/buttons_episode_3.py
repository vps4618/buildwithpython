from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDIconButton, MDFloatingActionButton


class ButtonsApp(MDApp):
    def build(self):
        screen = Screen()
        btn_flat = MDFlatButton(text="Hello World !", pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btn_flat1 = MDRectangleFlatButton(text="Hello World 1 !", pos_hint={'center_x': 0.2, 'center_y': 0.2})
        btn_flat2 = MDIconButton(icon="cactus", pos_hint={'center_x': 0.8, 'center_y': 0.8})
        btn_flat3 = MDIconButton(icon="language-python-text", pos_hint={'center_x': 0.6, 'center_y': 0.6})
        btn_flat4 = MDFloatingActionButton(icon="cake", pos_hint={'center_x': 0.3, 'center_y': 0.3})
        screen.add_widget(btn_flat)
        screen.add_widget(btn_flat1)
        screen.add_widget(btn_flat2)
        screen.add_widget(btn_flat3)
        screen.add_widget(btn_flat4)
        return screen


ButtonsApp().run()
