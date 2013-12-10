# -*- coding: utf-8 -*-

import kivy
import sale
import Login
kivy.require('1.7.2')
from kivy.app import App
from sale import UiManager
from sale import controller
from Login import login
from kivy.uix.screenmanager import ScreenManager, Screen


class BetaUi(App):
	s_man = None
	derp = None
	def build(self):
		self.s_man = ScreenManager()
		screen1 = login.coneccion()
		screen2 = Screen(name="screen2")
		temp = UiManager.Interfaz()
		screen2.add_widget(temp)
		self.s_man.add_widget(screen1)
		self.s_man.add_widget(screen2)
		return self.s_man


if __name__ =='__main__':
	BetaUi().run()