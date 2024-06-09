from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        self.CharacterLabel = Label(text="Welcome to the Game!", font_size='20sp')
        layout.add_widget(self.CharacterLabel)

        self.AcceptButton = Button(text="Accept", font_size='20sp')
        layout.add_widget(self.AcceptButton)

        self.NextButton = Button(text="Next", font_size='20sp')
        layout.add_widget(self.NextButton)

        self.add_widget(layout)
