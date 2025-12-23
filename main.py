from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class DevriyeApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        baslik = Label(
            text='NFC Devriye Takip',
            size_hint=(1, 0.3),
            font_size='28sp'
        )
        
        durum = Label(
            text='Hazir - NFC karti okutun',
            size_hint=(1, 0.4),
            font_size='20sp'
        )
        
        btn = Button(
            text='Test',
            size_hint=(1, 0.3),
            font_size='18sp'
        )
        
        layout.add_widget(baslik)
        layout.add_widget(durum)
        layout.add_widget(btn)
        
        return layout

if __name__ == '__main__':
    DevriyeApp().run()
