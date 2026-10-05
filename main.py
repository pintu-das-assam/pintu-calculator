from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class Calculator(App):

    def build(self):
        self.expression = ""

        main = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10
        )

        self.display = Label(
            text="0",
            font_size=40,
            size_hint_y=0.25
        )
        main.add_widget(self.display)

        grid = GridLayout(
            cols=4,
            spacing=5
        )

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]

        for value in buttons:
            button = Button(
                text=value,
                font_size=28
            )
            button.bind(on_press=self.button_pressed)
            grid.add_widget(button)

        main.add_widget(grid)
        return main

    def button_pressed(self, button):
        value = button.text

        if value == "C":
            self.expression = ""
            self.display.text = "0"

        elif value == "=":
            try:
                result = eval(self.expression)
                self.expression = str(result)
                self.display.text = self.expression
            except:
                self.expression = ""
                self.display.text = "Error"

        else:
            self.expression += value
            self.display.text = self.expression


Calculator().run()