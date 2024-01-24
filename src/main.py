from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:
    MDBottomAppBar:

        MDFabBottomAppBarButton:
            icon: "plus"
'''


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)


Example().run()