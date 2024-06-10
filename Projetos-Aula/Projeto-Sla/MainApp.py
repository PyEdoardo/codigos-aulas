from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class MeuBoxLayout(BoxLayout):
    pass

class MainApp(App):
    def build(self):
        return MeuBoxLayout()

MainApp().run()