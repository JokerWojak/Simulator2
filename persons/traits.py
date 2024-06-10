from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
import random

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
        max_height = self.height * 0.7  # Keep some space for labels

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

class BarGraphApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.bar_graph = BarGraphWidget(size_hint=(1, 0.8))
        layout.add_widget(self.bar_graph)

        button_layout = BoxLayout(size_hint=(1, 0.2))
        update_button = Button(text='Update Characteristics', size_hint=(1, 1))
        update_button.bind(on_release=self.update_characteristics)
        button_layout.add_widget(update_button)

        layout.add_widget(button_layout)
        return layout

    def update_characteristics(self, instance):
        new_values = {
            'Health': random.randint(0, 100),
            'Smarts': random.randint(0, 100),
            'Looks': random.randint(0, 100),
            'Happiness': random.randint(0, 100)
        }
        self.bar_graph.update_characteristics(new_values)

if __name__ == '__main__':
    BarGraphApp().run()
