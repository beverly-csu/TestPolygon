from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader


class TestSoundScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.sound_1 = SoundLoader.load('sounds/sound_1.wav')
        self.sound_2 = SoundLoader.load('sounds/sound_2.wav')

        self.btn_1 = Button(text='Проиграть звук №1', size_hint=(.8, .3), pos_hint={'center_x': .5})
        self.btn_1.on_press = self.on_press_btn_1

        self.btn_2 = Button(text='Проиграть звук №2', size_hint=(.8, .3), pos_hint={'center_x': .5})
        self.btn_2.on_press = self.on_press_btn_2

        layout = BoxLayout(orientation='vertical', spacing=6, size_hint=(.8, .3), pos_hint={'center_x': .5, 'center_y': .5})
        layout.add_widget(self.btn_1)
        layout.add_widget(self.btn_2)

        self.add_widget(layout)

    def on_press_btn_1(self):
        self.sound_1.play()

    def on_press_btn_2(self):
        self.sound_2.play()


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TestSoundScr())
        return sm


MyApp().run()
