from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob
from datetime import datetime
from pathlib import Path
import random
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

Builder.load_file('designe.kv')

class LoginScreen(Screen):
    def login(self, username, password):
        with open(r'C:\Users\zieba\Desktop\python\10appCourse\kivy_app\users.json') as file:
            users = json.load(file)

        if username in users and users[username]['password'] == password:
            self.manager.current = "login_screen_success"
        else:
            self.ids.wrong_login.text = "Wrong credentials!!!"

    def sign_up(self):
        self.manager.current = "signup_screen"

class SignUpScreen(Screen):
    def add_user(self, username, password):
        with open(r'C:\Users\zieba\Desktop\python\10appCourse\kivy_app\users.json') as file:
            users = json.load(file)

        users[username] = {
            "username": username, 
            "password": password, 
            "created": datetime.now().strftime("%Y-%m-%d %H-%M-%S")
            }
        
        with open(r'C:\Users\zieba\Desktop\python\10appCourse\kivy_app\users.json', 'w') as file:
            json.dump(users, file)
        
        self.manager.current = "signup_screen_successul"

        print(users)

class SignUpScreenSuccess(Screen):
    def login_page(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

class LoginScreenSuccess(Screen):
    def get_text(self, user_text):
        user_text = user_text.lower()
        
        #glob - extracts files path with absolute paths. Creates a list of those paths
        available_files = glob.glob(r'C:\Users\zieba\Desktop\python\10appCourse\kivy_app\texts\*')

        #Path(path).stem - extracts file names withou extentions.
        #eq. 'C:\\Users\\zieba\\Desktop\\python\\10appCourse\\kivy_app\\texts\\happy.txt' -> happy
        available_paths = [Path(path).stem for path in available_files]

        if user_text in available_paths:
            with open(r"C:\Users\zieba\Desktop\python\10appCourse\kivy_app\texts\{}.txt".format(user_text), encoding="utf8") as file:
                texts_in_file = file.readlines()
            self.ids.user_output.text = random.choice(texts_in_file)
        else:
            self.ids.user_output.text = "Quote not found, sorry :/"

    def logout(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__=="__main__":
    MainApp().run()