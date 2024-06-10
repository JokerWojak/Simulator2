import random
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color
from persons.character import Person

class BarGraphWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(BarGraphWidget, self).__init__(**kwargs)
        self.characteristics = {
            'Health': 0,
            'Smarts': 0,
            'Looks': 0,
            'Happiness': 0
        }
        self.colors = {
            'Health': (1, 0, 0, 1),  # Red
            'Smarts': (0, 1, 0, 1),  # Green
            'Looks': (0, 0, 1, 1),   # Blue
            'Happiness': (1, 1, 0, 1) # Yellow
        }
        self.labels = {}
        self.draw_bars()

    def draw_bars(self):
        self.canvas.clear()
        bar_width = self.width / len(self.characteristics)
        max_height = self.height * 0.6  # Adjusted to keep space for labels above and below

        with self.canvas:
            for i, (characteristic, value) in enumerate(self.characteristics.items()):
                Color(*self.colors[characteristic])
                bar_height = (value / 100) * max_height
                x = i * bar_width
                y = 0
                Rectangle(pos=(x, y), size=(bar_width, bar_height))

        self.draw_labels(bar_width, max_height)

    def draw_labels(self, bar_width, max_height):
        for label in self.labels.values():
            self.remove_widget(label)

        self.labels.clear()

        for i, (characteristic, value) in enumerate(self.characteristics.items()):
            label_text = f"{characteristic}: {value}"
            label = Label(text=label_text, size_hint=(None, None), size=(bar_width, 20), halign='center', valign='middle')
            label.text_size = label.size
            label.x = i * bar_width
            label.y = max_height + 20  # Position above the bars
            self.labels[characteristic] = label
            self.add_widget(label)

    def update_characteristics(self, new_values):
        self.characteristics.update(new_values)
        self.draw_bars()

    def on_size(self, *args):
        self.draw_bars()

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.character_label = Label(text=f'{Person().create_full_name()}', font_size='20sp', size_hint=(1, None), height=50)
        layout.add_widget(self.character_label)

        self.bar_graph = BarGraphWidget(size_hint=(1, 0.6))
        layout.add_widget(self.bar_graph)

        button_layout = BoxLayout(size_hint=(1, None), height=50, orientation='horizontal', spacing=10)
        self.accept_button = Button(text="Accept", font_size='20sp')
        button_layout.add_widget(self.accept_button)

        self.next_button = Button(text="Next", font_size='20sp')
        button_layout.add_widget(self.next_button)

        self.next_button.bind(on_release=self.update_name)

        layout.add_widget(button_layout)
        self.add_widget(layout)

    def update_name(self, *args):
        self.character_label.text = f'{Person().create_full_name()}'
        new_values = {
            'Health': random.randint(0, 100),
            'Smarts': random.randint(0, 100),
            'Looks': random.randint(0, 100),
            'Happiness': random.randint(0, 100)
        }
        self.bar_graph.update_characteristics(new_values)

class TestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        return sm

if __name__ == '__main__':
    TestApp().run()
