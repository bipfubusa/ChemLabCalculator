from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.metrics import dp

from chemistry import (
    calculate_molar_mass,
    calculate_concentration,
    calculate_dilution
)


class ChemLabApp(App):

    def build(self):
        self.title = "ChemLab Calculator"
        Window.clearcolor = (0.05, 0.09, 0.15, 1)

        root = BoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(12)
        )

        root.add_widget(Label(
            text="[b]ChemLab Calculator[/b]",
            markup=True,
            font_size="26sp",
            size_hint_y=None,
            height=dp(55)
        ))

        root.add_widget(Label(
            text="CHEMISTRY LABORATORY TOOLS",
            font_size="12sp",
            color=(0.4, 0.85, 0.75, 1),
            size_hint_y=None,
            height=dp(30)
        ))

        options = [
            ("Molar Mass", self.molar_mass_screen),
            ("Molar Concentration", self.concentration_screen),
            ("Dilution Calculator", self.dilution_screen),
        ]

        for title, action in options:
            button = Button(
                text=title,
                font_size="17sp",
                size_hint_y=None,
                height=dp(60),
                background_normal="",
                background_color=(0.10, 0.35, 0.42, 1)
            )
            button.bind(on_release=action)
            root.add_widget(button)

        root.add_widget(Label(
            text="CHEMISTRY • CALCULATIONS • PRECISION",
            font_size="10sp",
            size_hint_y=None,
            height=dp(30)
        ))

        return root

    def show_tool(self, title, fields, calculate):
        content = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(10)
        )

        inputs = {}

        for key, prompt in fields:
            content.add_widget(Label(
                text=prompt,
                size_hint_y=None,
                height=dp(30)
            ))

            field = TextInput(
                multiline)
