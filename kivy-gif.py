from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock


class Gif(Image):
    def __init__(self, frames=[], interval=1.0, **kwargs):
        super().__init__(source=frames[0], **kwargs)
        self.frames = frames
        self.interval = interval
        self.is_active = True
        self.index = 0
        self.start()

    def change_frame(self, dt):
        self.index += 1
        if self.index >= len(self.frames):
            self.index = 0
        self.source = self.frames[self.index]

    def start(self):
        self.is_active = True
        self.event = Clock.schedule_interval(self.change_frame, self.interval)

    def stop(self):
        self.is_active = False
        self.event.cancel()


class TestGifScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        frames = ['imgs/0.png', 'imgs/1.png',
                  'imgs/2.png', 'imgs/3.png', 'imgs/4.png']
        self.gif = Gif(frames, .1)

        self.btn = Button(text='Стоп', size_hint=(.3, .1), pos_hint={'center_x': .5})
        self.btn.on_press = self.btn_press

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(self.gif)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def btn_press(self):
        if self.gif.is_active:
            self.btn.text = 'Старт'
            self.gif.stop()
        else:
            self.btn.text = 'Стоп'
            self.gif.start()


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TestGifScreen())
        return sm


MyApp().run()