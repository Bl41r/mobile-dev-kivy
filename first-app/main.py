"""Following Kivy tutorials."""
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

kivy.require("1.8.0")


class LoginScreen(GridLayout):
    """Login screen."""

    def __init__(self, **kwargs):
        """Init."""
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Username:"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text="Password:"))
        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)

        self.add_widget(Label(text="Two Factor Auth:"))
        self.tfa = TextInput(multiline=False)
        self.add_widget(self.tfa)


class SimpleKivy(App):
    """App class."""

    def build(self):
        """Build our app."""
        return LoginScreen()

if __name__ == "__main__":
    SimpleKivy().run()
