# screens/widgets.py

from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color
from kivy.uix.label import Label

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
            'Health': (1, 0, 0, 1),    # Red
            'Smarts': (0, 1, 0, 1),    # Green
            'Looks': (0, 0, 1, 1),     # Blue
            'Happiness': (1, 1, 0, 1)  # Yellow
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
