import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from screens.welcome import WelcomeScreen  # Import WelcomeScreen

kivy.require('2.0.0')


class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_menu()

    def create_menu(self):
        # Create the root layout
        root = FloatLayout()

        # Create a BoxLayout for the buttons
        button_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None))
        button_layout.size = (200, 120)  # Width: 200, Height: 2 buttons * 50 + spacing

        # Center the BoxLayout
        button_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        # Create the buttons
        load_game_button = Button(text='Load Game', size_hint=(1, None), height=50)
        new_game_button = Button(text='New Game', size_hint=(1, None), height=50)

        # Bind the buttons to their respective functions
        load_game_button.bind(on_release=self.load_game)
        new_game_button.bind(on_release=self.new_game)

        # Add buttons to the BoxLayout
        button_layout.add_widget(load_game_button)
        button_layout.add_widget(new_game_button)

        # Add the BoxLayout to the root layout
        root.add_widget(button_layout)
        self.add_widget(root)

    def load_game(self, instance):
        print("Load Game button pressed")
        # Placeholder for load game logic
        App.get_running_app().start_game('load')

    def new_game(self, instance):
        print("New Game button pressed")
        # Navigate to Welcome Screen
        self.manager.current = 'welcome'
        App.get_running_app().start_game('new')


class GameApp(App):
    def build(self):
        self.title = 'Game Menu'

        sm = ScreenManager()

        # Add screens to the ScreenManager
        sm.add_widget(MainMenuScreen(name='main_menu'))
        sm.add_widget(WelcomeScreen(name='welcome'))

        sm.current = 'main_menu'  # Set the initial screen

        return sm

    def start_game(self, mode):
        print(f"Starting game in {mode} mode")
        # Placeholder for the game loop logic
        Clock.schedule_interval(self.run_game_loop, 1.0 / 60.0)  # 60 FPS

    def run_game_loop(self, dt):
        # Placeholder for the main game loop
        # This is where the game logic would go
        # dt is the time elapsed since the last frame
        pass


if __name__ == '__main__':
    GameApp().run()
