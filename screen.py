from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 500)

screen_helper = """
Screen:
    BoxLayout:
        Zoom:

    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Demo Application'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["dots-vertical", lambda x: app.navigation_draw()], ["clock", lambda x: app.navigation_draw()]]
            elevation:5

        MDLabel:
            text: ''
            halign: 'center'
            
        GridLayout:
            rows: 2
    
            Button:
                size_hint_y: 0.3
                text: 'You will be ok'
            
            
        MDBottomAppBar:
            MDToolbar:
                title: 'Demo'
                icon: 'language-python'
                type: 'bottom'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                on_action_button: app.navigation_draw()

"""


import zoom


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = Builder.load_string(screen_helper)
        # screen = Builder.load_file('screen.kv')

        return screen

    def navigation_draw(self):
        print("Navigation")


if __name__ == '__main__':
    DemoApp().run()