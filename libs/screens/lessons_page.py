from kivymd.uix.screen import MDScreen
import json
from libs.components.post_card import PostCard
a = ""
class LessonsPage(MDScreen):

    def list_posts(self):
        with open(r"lessons.json", "r") as f_obj:
            b = 0
            data = json.load(f_obj)
            for numberlesson in data:
                b = int(numberlesson)
                self.ids.timeline.add_widget(PostCard(
                    textlesson=data[numberlesson]["lessontext"],
                    titlel=data[numberlesson]["title"],
                ))

    def checkf(self):
        global a
        if a == "": #если переменная пустая записываем в неё значение
            self.list_posts()
            a = "123"

    def on_enter(self):
        self.checkf()



