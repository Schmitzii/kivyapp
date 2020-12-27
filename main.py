from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder

class DemoApp(MDApp):

    def build(self):
        username_helper="""
MDTextField:
    hint_text: "Enter username"
    helper_text: "forgot username"
    helper_text_mode: "on_focus"
    icon_right: "account"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {"center_x": 0.5, "center_y": 0.5}
    size_hint_x: None
    width: 300
"""

        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.primary_hue = "700"
        self.theme_cls.theme_style = "Light"
        screen = Screen()

       # username = MDTextField(text="Enter username", pos_hint={"center_x": 0.5, "center_y": 0.5}, size_hint_x=None, width=300)
        
        button = MDRectangleFlatButton(text="Show", pos_hint={"center_x": 0.5, "center_y": 0.4}, on_release=self.show_data)
                                        
        self.username = Builder.load_string(username_helper)

        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen
        
    def show_data(self, obj):
        if self.username.text is "":
            check_string = "Please enter a username"
        else:
            check_string = self.username.text + " does not exist"
        close_button = MDFlatButton(text="Close", on_release=self.close_dialog)
        more_button = MDFlatButton(text="More")
        self.dialog = MDDialog(title="Username Check", text=check_string, size_hint=(0.7, 1), buttons=[close_button, more_button])

        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


DemoApp().run()
