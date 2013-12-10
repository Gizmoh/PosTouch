# -*- coding: utf-8 -*-

import kivy
import sale
import PayUi
kivy.require('1.7.2')
from kivy.app import App
from sale import UiManager
from sale import controller
from PayUi import payment


class BetaUi(App):
	def build(self):
		derp = UiManager.Interfaz()
		return derp


if __name__ =='__main__':
	BetaUi().run()