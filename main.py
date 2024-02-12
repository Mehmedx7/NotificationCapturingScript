import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class HelloWorldApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        button = Button(text='Print Hello World', on_press=self.print_hello_world)
        layout.add_widget(button)
        return layout

    def print_hello_world(self, instance):
        print("Hello, World!")

if __name__ == '__main__':
    HelloWorldApp().run()
