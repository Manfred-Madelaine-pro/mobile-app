import random
import datetime

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.image import Image, AsyncImage

red = [1, 0, 0, 1]
blue = [0, 0, 1, 1]
green = [0, 1, 0, 1]
purple = [1, 0, 1, 1]


FEELING_WHEEL = "img/feelings.png"

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)

        im = Image(source=FEELING_WHEEL)
        layout.add_widget(im)

        layout.add_widget(Label(text='How do you feel today?'))

        datetime_object = datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
        layout.add_widget(Label(text=f'Current date and time is: {datetime_object}'))

        colors = [red, green, blue, purple]
        feelings = ["Good :)", "Funny :D", "Sad :/", "Bad :("]

        for feeling in feelings:
            btn = Button(text=feeling,
                         background_color=random.choice(colors)
                         )

            layout.add_widget(btn)

        layout.add_widget(Label(text='Would you like to save a comment?'))
        self.comment = TextInput(multiline=False)
        layout.add_widget(self.comment)

        save_button = Button(text='Save how you feel',
                     pos_hint={'center_x':0.5, 'center_y':0.5},
                     on_press=self.on_press_button
                     )
        layout.add_widget(save_button)
        return layout

    def on_press_button(self, obj):
        print('You pressed the save button!')
        datetime_object = datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
        print(f"You are feeling {obj.text} at {datetime_object} and commented that {self.comment.text}")


if __name__ == '__main__':
    app = MainApp()
    app.run()

# Question label: How do you feel mister XXX ?
# DateTime label
# Humeur dropdown choice
# Detail Text box
# Save button
