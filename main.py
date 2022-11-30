from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.uix.button import ButtonBehavior


from libs.screens.home_page import HomePage
from libs.screens.start_page import StartPage

class KivyApp(MDApp):
    def build(self):
        Window.size = [360, 800]
        self.load_all_kv_files()
        return StartPage()
    def load_all_kv_files(self):
        Builder.load_file('libs/screens/home_page.kv')
        Builder.load_file('libs/components/appbar.kv')
        Builder.load_file('libs/screens/start_page.kv')

if __name__ == "__main__":
    KivyApp().run()