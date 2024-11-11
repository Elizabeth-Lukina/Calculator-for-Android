from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


class MainApp(App):
    def build(self):
        # Устанавливаем цвет фона окна
        Window.clearcolor = (1, 0.8, 0.9, 1)  # Розоватый цвет фона

        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        main_layout.add_widget(self.solution)

    

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    background_color=(1, 0.6, 0.8, 1)  # Розовый цвет кнопок
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            self.solution.text = ""
        elif button_text == "=":
            # Вычисляем результат
            try:
                self.solution.text = str(eval(current.replace("^2", "**2").replace("%", "/100")))
            except Exception:
                self.solution.text = "Error"
        elif button_text == "+/-":
            # Инвертируем знаки числа
            if current:
                if current[0] == '-':
                    self.solution.text = current[1:]
                else:
                    self.solution.text = '-' + current
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                self.solution.text += button_text
                self.last_button = button_text

            self.last_was_operator = button_text in self.operators


if __name__ == "__main__":
    MainApp().run()