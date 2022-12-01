from kivymd.uix.screen import MDScreen

from kivy.lang.builder import Builder

from libs.screens.home_page import HomePage

class StartPage(MDScreen):
    def btn_clk(self):
        self.load_all_kv_files()
        return HomePage

    def load_all_kv_files(self):
        Builder.load_file('libs/screens/home_page.kv')
    '''Start Page'''
