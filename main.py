from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout  # Import FloatLayout
from kivy.clock import Clock
from screens.welcome import WelcomeScreen
from screens.game import GameScreen
import random
from persons.character import Person  # Assuming you have defined Person class

class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_menu()

    def create_menu(self):
        root = FloatLayout()

        button_layout = FloatLayout(size_hint=(None, None), size=(200, 120))
        button_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        load_game_button = Button(text='Load Game', size_hint=(None, None), size=(100, 50), pos=(50, 50))
        new_game_button = Button(text='New Game', size_hint=(None, None), size=(100, 50), pos=(50, 0))

        load_game_button.bind(on_release=self.load_game)
        new_game_button.bind(on_release=self.new_game)

        button_layout.add_widget(load_game_button)
        button_layout.add_widget(new_game_button)

        root.add_widget(button_layout)
        self.add_widget(root)

    def load_game(self, instance):
        print("Load Game button pressed")
        App.get_running_app().start_game('load')

    def new_game(self, instance):
        print("New Game button pressed")
        self.manager.current = 'welcome'
        App.get_running_app().start_game('new')

class GameApp(App):
    def build(self):
        self.title = 'Game Menu'

        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name='main_menu'))
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(GameScreen(name='game'))

        sm.current = 'main_menu'

        return sm

    def start_game(self, mode):
        print(f"Starting game in {mode} mode")
        game_screen = self.root.get_screen('game')
        if mode == 'load':
            # Placeholder for loading game state
            game_state = {
                'name': 'Loaded Character',
                'traits': {
                    'Health': 80,
                    'Smarts': 60,
                    'Looks': 70,
                    'Happiness': 90
                }
            }
            game_screen.load_game(game_state)
        elif mode == 'new':
            # Placeholder for creating a new character
            new_character = Person()
            game_screen.character_label.text = new_character.create_full_name()
            new_values = {
                'Health': random.randint(0, 100),
                'Smarts': random.randint(0, 100),
                'Looks': random.randint(0, 100),
                'Happiness': random.randint(0, 100)
            }
            game_screen.update_characteristics(new_values)

if __name__ == '__main__':
    GameApp().run()
