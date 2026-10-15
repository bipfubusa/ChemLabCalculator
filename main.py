from kivy.app import App
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

from chemistry import (
    calculate_molar_mass,
    calculate_concentration,
    calculate_dilution,
)


class ChemLabApp(App):

    def build(self):
        self.title = "ChemLab Calculator"
        Window.clearcolor = (0.05, 0.09, 0.15, 1)

        self.root = BoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(12),
        )

        self.show_menu()
        return self.root
    def show_menu(self):
        self.root.clear_widgets()

        self.root.add_widget(
            Label(
                text="[b]ChemLab Calculator[/b]",
                markup=True,
                font_size="26sp",
                size_hint_y=None,
                height=dp(60),
            )
        )

        self.root.add_widget(
            Label(
                text="CHEMISTRY LABORATORY TOOLS",
                font_size="12sp",
                color=(0.4, 0.85, 0.75, 1),
                size_hint_y=None,
                height=dp(30),
            )
        )

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
                background_color=(0.10, 0.35, 0.42, 1),
            )
            button.bind(on_release=action)
            self.root.add_widget(button)
    def show_tool(self, title, fields, calculate):
        self.root.clear_widgets()

        scroll = ScrollView()

        content = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(10),
            size_hint_y=None,
        )

        content.bind(minimum_height=content.setter("height"))

        content.add_widget(
            Label(
                text=f"[b]{title}[/b]",
                markup=True,
                font_size="22sp",
                size_hint_y=None,
                height=dp(50),
            )
        )

        inputs = {}

        for key, prompt in fields:
            content.add_widget(
                Label(
                    text=prompt,
                    size_hint_y=None,
                    height=dp(35),
                )
            )

            field = TextInput(
                multiline=False,
                size_hint_y=None,
                height=dp(48),
                hint_text=prompt,
            )

            inputs[key] = field
            content.add_widget(field)

        calculate_button = Button(
            text="Calculate",
            size_hint_y=None,
            height=dp(52),
        )

        def run_calculation(_button):
            try:
                result = calculate(inputs)
                self.show_message(title, result)
            except (ValueError, ZeroDivisionError) as error:
                self.show_message("Input Error", str(error))

        calculate_button.bind(on_release=run_calculation)
        content.add_widget(calculate_button)

        back_button = Button(
            text="Back to Menu",
            size_hint_y=None,
            height=dp(48),
        )

        back_button.bind(
            on_release=lambda _button: self.show_menu()
        )

        content.add_widget(back_button)
        scroll.add_widget(content)
        self.root.add_widget(scroll)
    def molar_mass_screen(self, _button=None):
        def calculate(inputs):
            formula = inputs["formula"].text.strip()

            mass = calculate_molar_mass(formula)

            return (
                f"Chemical formula: {formula}\n"
                f"Molar mass: {mass:.3f} g/mol"
            )

        self.show_tool(
            "Molar Mass",
            [
                ("formula", "Chemical formula (e.g. Ca(OH)2)")
            ],
            calculate,
        )
    def concentration_screen(self, _button=None):
        def calculate(inputs):
            try:
                mass = float(inputs["mass"].text.strip())
                molar_mass = float(inputs["molar_mass"].text.strip())
                volume = float(inputs["volume"].text.strip())
            except ValueError:
                raise ValueError(
                    "Enter valid numbers in all three fields."
                ) from None

            if not all(
                0 < value < float("inf")
                for value in (mass, molar_mass, volume)
            ):
                raise ValueError(
                    "All values must be positive and finite."
                )

            moles, concentration = calculate_concentration(
                mass, molar_mass, volume
            )

            return (
                f"Amount of substance: {moles:.4f} mol\n"
                f"Molar concentration: {concentration:.4f} mol/L"
            )

        self.show_tool(
            "Molar Concentration",
            [
                ("mass", "Solute mass (g)"),
                ("molar_mass", "Molar mass (g/mol)"),
                ("volume", "Solution volume (L)"),
            ],
            calculate,
        )
    def dilution_screen(self, _button=None):
        def calculate(inputs):
            try:
                c1 = float(inputs["c1"].text.strip())
                c2 = float(inputs["c2"].text.strip())
                v2 = float(inputs["v2"].text.strip())
            except ValueError:
                raise ValueError(
                    "Enter valid numbers in all three fields."
                ) from None

            if not all(
                0 < value < float("inf")
                for value in (c1, c2, v2)
            ):
                raise ValueError(
                    "All values must be positive and finite."
                )

            v1, water = calculate_dilution(c1, c2, v2)

            return (
                f"Stock solution needed: {v1:.2f} mL\n"
                f"Water to add: {water:.2f} mL"
            )

        self.show_tool(
            "Dilution Calculator",
            [
                ("c1", "Initial concentration (mol/L)"),
                ("c2", "Final concentration (mol/L)"),
                ("v2", "Final volume (mL)"),
            ],
            calculate,
        )
    def show_message(self, title, message):
        content = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(12),
        )

        content.add_widget(
            Label(text=message)
        )

        close_button = Button(
            text="Close",
            size_hint_y=None,
            height=dp(45),
        )

        popup = Popup(
            title=title,
            content=content,
            size_hint=(0.88, 0.45),
            auto_dismiss=False,
        )

        close_button.bind(on_release=popup.dismiss)
        content.add_widget(close_button)
        popup.open()
if __name__ == "__main__":
    ChemLabApp().run()
