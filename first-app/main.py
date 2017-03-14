"""Following Kivy tutorials."""
import kivy
from kivy.app import App
from kivy.uix.label import Label
kivy.require("1.8.0")


class SimpleKivy(App):
    """App class."""

    def build(self):
        """Build our app."""
        return Label(text="Hello World!")

if __name__ == "__main__":
    SimpleKivy().run()
