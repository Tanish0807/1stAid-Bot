# pip install kivymd 
# import kivymd
from kivymd.app import MDApp
# from kivymd.uix.screen import Screen
from kivy.lang import Builder
# from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.button import MDFlatButton
# from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
# from kivymd.uix.textfield import MDTextField
# from helper import username_input
import helper
import model


# from kivy.core.window import Window
# Window.size = (350,550)


class DemoApp(MDApp):
    def __init__(self):
        super().__init__()
        self.screen = Builder.load_string(helper.navigation_helper)

    def build(self):
        self.theme_cls.primary_palette = "Green"
        # screen = Screen()
        # button = MDRectangleFlatButton(text='Show', pos_hint={'center_x': 0.5, 'center_y': 0.4}
        #                               , on_release=self.show_data)
        # self.label = MDLabel(text="Hello, World", pos_hint={'center_x': 0.9, 'center_y': 0.3})
        # username = MDTextField(
        #     pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #     size_hint_x=None, width=200)
        # username = Builder.load_string(helpers.username_input)
        # self.username = Builder.load_string(helper.username_input)
        # screen.add_widget(self.username)
        # screen.Screen.MDNavigationLayout.ScreenManager.Screen.BoxLayout.add_widget(self.username)
        # self.screen.add_widget(button)
        # screen.add_widget(self.label)
        return self.screen

    def show_data(self):  # (self,obj):
        self.abc = model.chat(self.screen.ids.user_name.text)
        # self.abc = model.chat(self.username.text)
        # self.label.text = self.abc # self.username.text
        close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
        # more_button = MDFlatButton(text='More')
        self.dialog = MDDialog(title='First-aid Suggested..', text=self.abc,  # self.username.text,
                               size_hint=(0.7, 1),
                               buttons=[close_button])  # , more_button])
        self.dialog.open()
        # print(self.abc)

    def close_dialog(self, obj):
        self.dialog.dismiss()


DemoApp().run()
