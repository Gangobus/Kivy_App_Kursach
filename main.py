import json
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from libs.components.post_card import PostCard
from kivy.properties import StringProperty
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.card import MDCard



class StartPage(Screen):
    pass


class Plate(MDCard):
    _video_title = StringProperty("#01 Introduction to Kivymd & Toolbar")
    _channel_name = StringProperty("Sk Sahil - 79K views - 1 day ago")

    def on_kv_post(self, obj):
        pass

class LessonsPage(Screen):
    pass
    # def on_enter(self):
    #     self.list_lessons()
    # def list_lessons(self):
    #     with open('data/lessons.json') as f_obj:
    #         data = json.load(f_obj)
    #         for lessonnumber in data:
    #             self.ids.timeline.add_widget(PostCard(
    #                 postnumber=postnumber,
    #                 avatar=data[username]['avatar'],
    #                 post=data[username]['post'],
    #                 caption=data[username]['caption'],
    #                 likes=data[username]['likes'],
    #                 comments=data[username]['comments'],
    #                 posted_ago=data[username]['posted_ago'],
    #             ))


class TestsPage(Screen):
    pass

class GamePage(Screen):
    pass

class VideosPage(Screen):
    pass

class BottomNav(MDBoxLayout):
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
