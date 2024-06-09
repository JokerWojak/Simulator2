import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

kivy.require('2.0.0')


class GameApp(App):
    def build(self):
        self.title = 'Game Menu'

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

        return root

    def load_game(self, instance):
        print("Load Game button pressed")
        # Placeholder for load game logic
        self.start_game('load')

    def new_game(self, instance):
        print("New Game button pressed")
        # Placeholder for new game logic
        self.start_game('new')

    def start_game(self, mode):
        print(f"Starting game in {mode} mode")
        # Placeholder for the game loop logic
        self.run_game_loop()

    def run_game_loop(self):
        print("Running the game loop...")
        # Placeholder for the main game loop
        # This is where the game logic would go
        pass


if __name__ == '__main__':
    GameApp().run()
