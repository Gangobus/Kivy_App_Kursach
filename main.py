from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp


class StartPage(Screen):
    pass

class LessonsPage(Screen):
    pass

class TestsPage(Screen):
    pass

class GamePage(Screen):
    pass

class VideosPage(Screen):
    pass

class MyApp(MDApp):
    def build(self):
        Window.size = [360,720]
        Builder.load_file("libs/screens/start_page.kv")
        Builder.load_file("libs/screens/lessons_page.kv")
        Builder.load_file("libs/screens/tests_page.kv")
        Builder.load_file("libs/screens/game_page.kv")
        Builder.load_file("libs/screens/videos_page.kv")


        sm = ScreenManager()
        sm.add_widget(StartPage(name="Go"))
        sm.add_widget(LessonsPage(name="Lessons"))
        sm.add_widget(TestsPage(name="Tests"))
        sm.add_widget(GamePage(name="Game"))
        sm.add_widget(VideosPage(name="Videos"))
        return sm


MyApp().run()
