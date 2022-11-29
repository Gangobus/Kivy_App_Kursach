from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

class KivyApp(MDApp):
    def build(self):
        Window.size = [300, 600]
        label = Label(text = "Kivy")
        return label



if __name__ == "__main__":
    KivyApp().run()