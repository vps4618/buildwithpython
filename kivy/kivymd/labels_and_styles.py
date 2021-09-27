from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.boxlayout import MDBoxLayout


class VishwaApp(MDApp):
    def build(self):
        # theme colours in labels = Primary,Secondary,Hint,Error

        # Primary - less transparent
        # Secondary - more transparent than primary
        # Hint - more transparent than secondary
        # Error - red in colour

        layout = MDBoxLayout()

        label = MDLabel(text="Hello World", halign="center", theme_text_color="Error")
        label1 = MDLabel(text="Hello World 1", halign="center", theme_text_color="Primary")
        label2 = MDLabel(text="Hello World 2", halign="center", theme_text_color="Secondary")
        label3 = MDLabel(text="Hello World 3", halign="center", theme_text_color="Hint")

        # how to add custom colours
        label4 = MDLabel(text="Hello World 4", halign="center", theme_text_color="Custom", text_color=(0, 0, 1, 1))
        label5 = MDLabel(text="Hello World 5", halign="center", theme_text_color="Custom",
                         text_color=(162/255.0, 0/255.0, 162/255.0, 1))
        # font styles

        # H styles

        label6 = MDLabel(text="Hello World 6", halign="center", theme_text_color="Hint", font_style="H1")
        label7 = MDLabel(text="Hello World 7", halign="center", theme_text_color="Hint", font_style="H2")
        label8 = MDLabel(text="Hello World 8", halign="center", theme_text_color="Hint", font_style="H3")
        label9 = MDLabel(text="Hello World 9", halign="center", theme_text_color="Hint", font_style="H4")
        label10 = MDLabel(text="Hello World 10", halign="center", theme_text_color="Hint", font_style="H5")
        label11 = MDLabel(text="Hello World 11", halign="center", theme_text_color="Hint", font_style="H6")

        # subtitle styles

        label12 = MDLabel(text="Hello World 12", halign="center", theme_text_color="Hint", font_style="Subtitle1")
        label13 = MDLabel(text="Hello World 13", halign="center", theme_text_color="Hint", font_style="Subtitle2")

        # body styles

        label14 = MDLabel(text="Hello World 14", halign="center", theme_text_color="Hint", font_style="Body2")
        label15 = MDLabel(text="Hello World 15", halign="center", theme_text_color="Hint", font_style="Body2")

        # button,caption and overline styles
        label16 = MDLabel(text="Hello World 16", halign="center", theme_text_color="Hint", font_style="Button")
        label17 = MDLabel(text="Hello World 17", halign="center", theme_text_color="Hint", font_style="Caption")
        label18 = MDLabel(text="Hello World 18", halign="center", theme_text_color="Hint", font_style="Overline")
        label19 = MDLabel(text="Hello World 19", halign="center", theme_text_color="Hint", font_style="Icon")

        icon = MDIcon(icon="rocket", halign="center")
        layout.add_widget(label)
        layout.add_widget(label1)
        layout.add_widget(label2)
        layout.add_widget(label3)
        layout.add_widget(label4)
        layout.add_widget(label5)
        layout.add_widget(label6)
        layout.add_widget(label7)
        layout.add_widget(label8)
        layout.add_widget(label9)
        layout.add_widget(label10)
        layout.add_widget(label11)
        layout.add_widget(label12)
        layout.add_widget(label13)
        layout.add_widget(label14)
        layout.add_widget(label15)
        layout.add_widget(label16)
        layout.add_widget(label17)
        layout.add_widget(label18)
        layout.add_widget(label19)
        layout.add_widget(icon)


        return layout


VishwaApp().run()
