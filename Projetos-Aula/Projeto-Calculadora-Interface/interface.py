from kivy.app import App
from kivy.lang import Builder
import os.path

GUI = Builder.load_file("tela.kv")

class Aplicativo(App):
    def build(self):
        return GUI

Aplicativo().run()
