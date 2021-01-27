import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

red = [1, 0, 0, 1]
blue = [0, 0, 1, 1]
green = [0, 1, 0, 1]
purple = [1, 0, 1, 1]


class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)
        colors = [red, green, blue, purple]

        for i in range(5):
            btn = Button(text="Button #%s" % (i + 1),
                         background_color=random.choice(colors)
                         )

            layout.add_widget(btn)

        save_button = Button(text='Save how you feel',
                     pos_hint={'center_x':0.5, 'center_y':0.5},
                     on_press=self.on_press_button
                     )
        layout.add_widget(save_button)
        return layout

    def on_press_button(self, obj):
        print('You pressed the save button!')


if __name__ == '__main__':
    app = MainApp()
    app.run()

# Question label: How do you feel mister XXX ?
# DateTime label
# Humeur dropdown choice
# Detail Text box
# Save button
