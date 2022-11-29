from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivymd.icon_definitions import md_icons

from libs.screens.home_page import HomePage


class KivyApp(MDApp):
    def build(self):
        Window.size = [300, 600]
        self.load_all_kv_files()
        return HomePage()
    def load_all_kv_files(self):
        Builder.load_file('libs/screens/home_page.kv')



if __name__ == "__main__":
    KivyApp().run()