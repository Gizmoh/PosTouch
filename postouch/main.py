# -*- coding: utf-8 -*-

import kivy
import sale
import Login
import PayUi
kivy.require('1.7.2')
from kivy.app import App
from sale import UiManager
from sale import controller
from PayUi import payment
from Login import login
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SlideTransition


class BetaUi(App):
	s_man = None
	derp = None
	def build(self):
		self.s_man = ScreenManager()
		self.s_man.transition = SlideTransition()
		screen1 = login.coneccion()
		screen2 = Screen(name="screen2")
		screen3 = Screen(name="screen3")
		temp = UiManager.Interfaz()
		temp2 = payment.Payment()
		screen2.add_widget(temp)
		screen3.add_widget(temp2)
		self.s_man.add_widget(screen1)
		self.s_man.add_widget(screen2)
		self.s_man.add_widget(screen3)
		return self.s_man


if __name__ =='__main__':
	BetaUi().run()