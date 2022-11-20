from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
from random import randint
import requests
import os.path
import shutil


Builder.load_file('designe.kv')

class MainWindow(Screen):
    def get_img(self):
        search_item = self.manager.current_screen.ids.qwe.text
        page = wikipedia.page(search_item)
        url = page.images[1]
        return url

    def download_img(self):
        img_path = "files/img.jpg"
        r = requests.get(self.get_img(), stream=True)
        with open(img_path, 'wb') as f:
            f.write(r.content)
        return img_path

    def set_img(self):
        self.manager.current_screen.ids.img.source = self.download_img()

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

MainApp().run()