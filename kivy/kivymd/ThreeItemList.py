from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, ThreeLineListItem
from kivy.uix.scrollview import ScrollView


class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)
        for i in range(1, 21):
            lists = ThreeLineListItem(text="Item "+str(i), secondary_text="Hello World!",
                                      tertiary_text="Vishwa Praveen")
            list_view.add_widget(lists)
        screen.add_widget(scroll)
        return screen


DemoApp().run()
