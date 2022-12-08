import json
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
from kivy.uix.scrollview import ScrollView
import sqlite3
from libs.components.post_card import PostCard
from libs.screens.lessons_page import LessonsPage


class StartPage(Screen):
    pass

#class LessonsPage(Screen):

    # def on_enter(self):
    #     self.list_posts()
    # def list_posts(self):
    #     #with open('assets/data/posts.json') as f_obj:
    #     with open(r"lessons.json","r") as f_obj:
    #         data = json.load(f_obj)
    #         for lessonnumber in data:
    #             self.ids.timeline.add_widget(PostCard(
    #                 lessonnumber = lessonnumber,
    #                 postname = data[lessonnumber]['lessonname'],
    #                 posttext = data[lessonnumber]['lessontext'],
    #             ))
    # lessons_plik = open(r"data.txt","r")
    # fileoutput = StringProperty(lessons_plik.read())
    # lessons_plik.close()
    #
    #
    # def show_lessons(self):
    #     # Create Database Or Connect To One
    #     conn = sqlite3.connect('first_db.db')
    #
    #     # Create A Cursor
    #     c = conn.cursor()
    #
    #     # Grab records from database
    #     c.execute("SELECT * FROM lessons")
    #     records = c.fetchall()
    #
    #     lesson_name = ''
    #     lesson_text = ''
    #     lesson_number = 0
    #     # Loop thru records
    #     for row in records:
    #         lesson_number = f'{lesson_number}\n{row[0]}'
    #         lesson_name = f'{lesson_name}\n{row[1]}'
    #         lesson_text = f'{lesson_text}\n{row[2]}'
    #         self.ids.timeline.add_widget(PostCard())
    #         #self.ids.l_number.text = f'{lesson_number}'
    #         #self.ids.l_name.text = f'{lesson_name}'
    #         #self.ids.l_text.text = f'{lesson_text}'
    #
    #
    #
    #     # Commit our changes
    #     conn.commit()
    #
    #     # Close our connection
    #     conn.close()


class TestsPage(Screen):
    pass

class GamePage(Screen):
    pass

class VideosPage(Screen):
    pass

# class BottomNav(MDBoxLayout):
#     pass

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

    # def on_start(self):
    #     self.root.dispatch('on_enter')


MyApp().run()
