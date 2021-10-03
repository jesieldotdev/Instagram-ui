from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = 300, 500

class insta(MDApp):
	def build(self):
		self.theme_cls.theme_style = 'Dark'
		self.theme_cls.primary_pallete = 'Dark_Blue'

insta().run()