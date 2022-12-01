from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window

class StartPage(Screen):
    pass

class HomePage(Screen):
    pass

class LessonsPage(Screen):
    pass


class MyApp(MDApp):
    def build(self):
        Window.size = [360, 780]
        Builder.load_file("libs/screens/start_page.kv")
        Builder.load_file("libs/screens/home_page.kv")
        Builder.load_file("libs/screens/lessons_page.kv")

        sm = ScreenManager()
        sm.add_widget(StartPage(name="GO"))
        sm.add_widget(HomePage(name="Lessons"))
        sm.add_widget(HomePage(name="Tests"))
        sm.add_widget(LessonsPage(name="Back"))
        return sm

MyApp().run()