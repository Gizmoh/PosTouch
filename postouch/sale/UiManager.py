import kivy
import controller
kivy.require('1.7.2') # replace with your current kivy version !

from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.accordion import Accordion,AccordionItem
from kivy.uix.modalview import ModalView
from kivy.properties import ObjectProperty


class row(BoxLayout):#Objeto custom para la lista
	name = ObjectProperty(None)
	code = ObjectProperty(None)
	quantity = ObjectProperty(None)
	close = ObjectProperty(None)
	add = ObjectProperty(None)
	priceU = ObjectProperty(None)
	priceT = ObjectProperty(None)
	counter = 1
	price = ""



class CBoton (Button):#Boton custom para almacenar la informacion
	name = ""
	code = ""
	price = ""


class Interfaz(BoxLayout):#Interfaz Principal
	listA = []
	cost = 0

	def __init__(self,**kwargs):
		#Inicializacion de la interfaz
		super(Interfaz, self).__init__(**kwargs)
		#Definicion de Variables
		listB = []
		aux = 1
		box = ObjectProperty(None)
		txt = ObjectProperty(None)
		grid = ObjectProperty(None)
		discount = ObjectProperty(None)
		total = ObjectProperty(None)
		save = ObjectProperty(None)
		printAct = ObjectProperty(None)
		send = ObjectProperty(None)
		money = ObjectProperty(None)
		logOut = ObjectProperty(None)
		self.discount.bind(is_open = self.addDiscount)
		self.logOut.bind(on_press = self.LogOut)
		products = controller.get_products()
		users = controller.get_users()
		self.save.background_color = 0,147,0,.5
		self.save.bind(on_press = self.press)
		self.save.bind(on_release = self.release)
		self.send.background_color = 162,0,170,.5
		self.send.bind(on_release = self.releaseB)
		self.printAct.background_color = 162,0,170,.5
		self.printAct.bind(on_press = self.pressB)
		self.printAct.bind(on_release = self.releaseB)
		#Ingreso de usuarios al Spinner
		for i in users:
			listB.append(i.username)
		self.txt.text = listB[0]
		self.txt.values = listB
		#Ingreso de productos a la listA deslizante
		for fila in products:
			Q = CBoton()
			Q.background_color = 1,1,1,(aux%2+0.5)
			aux = aux+1
			Q.name = fila.name
			Q.text = fila.name[:20]
			Q.code = fila.supplier_code
			Q.precio = fila.gross_price
			Q.bind(on_press = self.addRow)
			self.grid.add_widget(Q)
			self.grid.bind(minimum_width=self.grid.setter('width'))



	def addRow(interfaz,self):#Agrega productos a la grid
		test = True
		temp = row()
		temp.name.text = (self.text)
		temp.code.text = (self.code)
		temp.priceU.text = ("$ "+str(self.precio))
		temp.precio = self.precio
		temp.priceT.text = format_price(self.precio*temp.counter)
		temp.close.bind(on_press= interfaz.removeStuff)
		temp.add.bind(on_press = interfaz.moarStuff)
		for tmp in interfaz.listA:
			if tmp.name.text == self.text:
				tmp.counter = tmp.counter + 1
				tmp.quantity.text = str(tmp.counter)
				tmp.priceT.text = format_price(self.precio*tmp.counter)
				test = False
				setPrice(interfaz)
		if test == True:
			interfaz.listA.append(temp)
			interfaz.box.add_widget(temp)
			interfaz.box.bind(minimum_height=interfaz.box.setter('height'))
			setPrice(interfaz)
		test = True

	def moarStuff(interfaz, self):#Agrega mas productos a elementos de la grid, mediante el boton
		self.parent.counter = self.parent.counter +1
		self.parent.quantity.text = str(self.parent.counter)
		self.parent.priceT.text = format_price(self.parent.precio*self.parent.counter)
		setPrice(interfaz)

	def removeStuff(interfaz,self):#Reduce y elimina productos de la grid
		self.parent.counter = self.parent.counter - 1
		self.parent.quantity.text = str(self.parent.counter)
		self.parent.priceT.text = format_price(self.parent.precio*self.parent.counter)
		if self.parent.counter == 0:
			interfaz.box.remove_widget(self.parent)
			interfaz.listA.remove(self.parent)
		setPrice(interfaz)

	def addDiscount(interfaz,self, value):#Calcula y aplica el descuento
		temp = interfaz.cost
		if temp == 0:
			pass
		if value == False:
			if float(self.text) > 0:
				temp = interfaz.cost - ((interfaz.cost)*int(self.text))/100
				interfaz.total.text = format_price(temp)
			if float(self.text) == 0:
				interfaz.total.text = format_price(interfaz.cost)

	def calcDiscount(self):
		self.addDiscount(self.discount,False)
		#Estas funciones hacen mas visible el efecto de apretar botones
	def press(interfaz, self):
		self.background_color = 0,147,0,.3

	def release(interfaz, self):
		self.background_color = 0,147,0,.5

	def pressB(interfaz, self):
		self.background_color = 162,0,170,.3

	def releaseB(interfaz, self):
		self.background_color = 162,0,170,.5

	def LogOut(interfaz, self):
		interfaz.parent.parent.transition.direction = "right"
		interfaz.parent.manager.current = "screen1"

	def PayUi(interfaz, self):
		interfaz.parent.parent.parent.Total = interfaz.cost
		interfaz.parent.parent.transition.direction = "left"
		interfaz.parent.manager.current = "screen3"

	#def DisplaySale(interfaz,self):#Despliega la ventana de transacciones
	#	Checkout = PayUi()
	#	Checkout.subtotal.text = interfaz.total.text
	#	Checkout.open()


def setPrice(interfaz):#Sets prices
	temp = 0
	#print(interfaz.money.text)
	for i in interfaz.listA:
		temp = temp + i.precio*i.counter
	interfaz.money.text = format_price(temp)
	interfaz.cost = temp
	interfaz.calcDiscount()

def format_float(n, decimals=1):#Le da formato a los strings con dinero
    """float -> string"""
    t = {",": ".", ".": ","}
    return "".join(t.get(c, c) for c in format(n, ",.{}f".format(decimals)))


def format_price(p, sym="$", decimals=0):
    """int -> string"""
    if sym == "CL":
        sym = "$"
    return u"{0} {1}".format(sym, format_float(p, decimals=decimals))



def Check(self):#Revisa la lista por si el row a agregar ya existe
	if self.listA.__contains__(self.text)==True:
		pass
