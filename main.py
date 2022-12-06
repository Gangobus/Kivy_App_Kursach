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


class StartPage(Screen):
    pass


class Plate(MDCard):
    _video_title = StringProperty("#01 Introduction to Kivymd & Toolbar")
    _channel_name = StringProperty("Sk Sahil - 79K views - 1 day ago")

    def on_kv_post(self, obj):
        pass

class LessonsPage(Screen):

    lessons_plik = open(r"data.txt","r")
    fileoutput = StringProperty(lessons_plik.read())
    lessons_plik.close()

    def show_records(self):
        # Create Database Or Connect To One
        conn = sqlite3.connect('first_db.db')

        # Create A Cursor
        c = conn.cursor()

        # Grab records from database
        c.execute("SELECT * FROM customers")
        records = c.fetchall()

        word = ''
        # Loop thru records
        for record in records:
            word = f'{word}\n{record[0]}'
            self.root.ids.word_label.text = f'{word}'

        # Commit our changes
        conn.commit()

        # Close our connection
        conn.close()


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
