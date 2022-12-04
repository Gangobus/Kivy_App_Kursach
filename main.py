from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp


class StartPage(Screen):
    pass


class HomePage(Screen):
    pass


class LessonsPage(Screen):
    pass

class TestsPage(Screen):
    pass


class MyApp(MDApp):
    def build(self):
        Window.size = [300,600]
        Builder.load_file("libs/screens/start_page.kv")
        #Builder.load_file("libs/screens/home_page.kv")
        Builder.load_file("libs/screens/lessons_page.kv")
        Builder.load_file("libs/screens/tests_page.kv")

        sm = ScreenManager()
        sm.add_widget(StartPage(name="Go"))
        #sm.add_widget(HomePage(name="Homepg"))
        #sm.add_widget(HomePage(name="Homepg"))
        sm.add_widget(LessonsPage(name="Lessons"))
        sm.add_widget(TestsPage(name="Tests"))
        return sm


MyApp().run()
