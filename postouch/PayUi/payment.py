# -*- coding: utf-8 -*-
import kivy
kivy.require('1.7.2')
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

class Selector(Accordion):
	subtotal = ObjectProperty(None)

class Payment(BoxLayout):
	def __init__(self,**kwargs):
		super(Payment, self).__init__(**kwargs)
		Select = Selector()
		self.add_widget(Select)
		Selector.subtotal = self.root.Total()