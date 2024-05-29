from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
def on_press(btn):
    btn.text = 'apertado'

def on_release(btn):
    btn.text = 'solto!'

class MeuApp(App):
    def build(self):
        box1 = BoxLayout(orientation='vertical')
        label = Label(text='Olá Mundo!')
        label.font_size = 50

        text_input = TextInput()

        btn = Button(
            text='Butaum', 
            on_press=on_press,
            on_release=on_release
            )
        btn.font_size = 50
        box1.add_widget(label)
        box1.add_widget(text_input)
        box1.add_widget(btn)
        return box1

MeuApp().run()