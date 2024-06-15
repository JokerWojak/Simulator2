from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color
from kivy.properties import ObjectProperty
from screens.widgets import BarGraphWidget
from persons.character import Person

class GameScreen(Screen):
    save_button = ObjectProperty(None)
    character_label = ObjectProperty(None)
    bar_graph = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.character_label = Label(text="Character Name", font_size='20sp', size_hint=(1, None), height=50)
        layout.add_widget(self.character_label)

        self.bar_graph = BarGraphWidget(size_hint=(1, 0.6))
        layout.add_widget(self.bar_graph)

        button_layout = BoxLayout(size_hint=(1, None), height=50, orientation='horizontal', spacing=10)
        self.save_button = Button(text="Save Game", font_size='20sp')
        self.save_button.bind(on_release=self.save_game)
        button_layout.add_widget(self.save_button)

        self.empty_buttons = []
        for i in range(5):
            empty_button = Button(text=f'Empty Button {i+1}', font_size='20sp')
            self.empty_buttons.append(empty_button)
            button_layout.add_widget(empty_button)

        layout.add_widget(button_layout)
        self.add_widget(layout)

    def update_characteristics(self, new_values):
        self.bar_graph.update_characteristics(new_values)

    def save_game(self, instance):
        first_name, last_name = self.character_label.text.split()
        save_data = {
            'first_name': first_name,
            'last_name': last_name,
            'traits': self.bar_graph.characteristics
        }
        # Placeholder: Save data to a file (implement your saving logic here)
        print(f"Saving game data: {save_data}")

    def load_game(self, game_state):
        self.character_label.text = game_state['name']
        self.bar_graph.update_characteristics(game_state['traits'])
