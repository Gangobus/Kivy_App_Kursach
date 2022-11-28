from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class MyApp(App):
    def build(self):
        label = Label(text = "test text")
        return label
app = MyApp()
app.run()
