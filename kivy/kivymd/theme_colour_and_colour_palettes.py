from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import Screen


class ThemecolourApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Yellow"  # palette change colour of buttons
        self.theme_cls.primary_hue = "A700"  # hue standers for darkness of the colour of the button
        self.theme_cls.theme_style = "Dark"  # this will darken the window
        screen = Screen()
        btn1 = MDRectangleFlatButton(text="Hello World", pos_hint={"center_x": 0.5, "center_y": 0.5})
        screen.add_widget(btn1)
        return screen


ThemecolourApp().run()
