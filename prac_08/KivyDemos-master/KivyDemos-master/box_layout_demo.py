from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """
        Handler for pressing entry buttons
        :param: the Kivy button instance
        :return: None
        """
        print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear_text(self, input_name):
        """
        Clear any buttons that have been selected (visually) and reset status text
        :return: None
        """
        self.root.ids.output_label.text = ""
        input_name.text = ""


BoxLayoutDemo().run()
