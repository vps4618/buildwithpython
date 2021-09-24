from kivymd.app import MDApp
from kivymd.uix.label import MDIcon
from kivymd.uix.boxlayout import MDBoxLayout


class IconApp(MDApp):
    def build(self):
        layout = MDBoxLayout()
        icon1 = MDIcon(icon='account-cash', halign='center')
        icon2 = MDIcon(icon='account-child', halign='center')
        icon3 = MDIcon(icon="airballoon", halign='center')
        icon4 = MDIcon(icon="airplane", halign='center')
        layout.add_widget(icon1)
        layout.add_widget(icon2)
        layout.add_widget(icon3)
        layout.add_widget(icon4)
        return layout


IconApp().run()
