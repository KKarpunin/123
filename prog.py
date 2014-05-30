
import os
import sys
import random
import gtk


class Window:

	def __init__(self):
		"""
		Главный конструктор.
		"""
		self.Dialog()

	def Dialog(self):
		"""
		Создается окно с тремя полями ввода текста.
		В первом пользователь вводит текст, во втором программа кодирует введенный текст
		и выводит закодированный текст во второе поле, в третьем поле выводится
		случайное число.
		"""
		self.MainDialog = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.MainDialog.set_title("My App for 4")
		self.MainDialog.set_default_size(500,100)
		self.MainDialog.set_position(gtk.WIN_POS_CENTER_ALWAYS)
		self.MainDialog.activate_focus()
		self.image = gtk.Image()
		self.image.show()            
		self.vbox = gtk.VBox(False, 20)
		self.MainDialog.add(self.vbox)
		self.LabelIn = gtk.Label("Исходный текст.")
		self.LabelOut = gtk.Label("Кодированный текст.")
		self.LabelOut_In = gtk.Label("Случайное число")
		self.In = gtk.Entry(max = 32)
		self.Out = gtk.Entry(max = 32)
		self.Out_In = gtk.Entry()
		self.vbox.pack_start(self.image, True, True, 0)
		self.vbox.pack_start(self.LabelIn, True, True, 0)
		self.vbox.pack_start(self.In, True, True, 0)
		self.vbox.pack_start(self.LabelOut, True, True, 0)
		self.vbox.pack_start(self.Out, True, True, 0)
		self.vbox.pack_start(self.LabelOut_In, True, True, 0)
		self.vbox.pack_start(self.Out_In, True, True, 0)
		self.bbox = gtk.HButtonBox ()
		self.vbox.pack_start(self.bbox, False, False, 0)
		self.bbox.set_layout(gtk.BUTTONBOX_EDGE)
		self.button = gtk.Button("Encrypt")
		self.Button_rand = gtk.Button("Random")
		self.button.connect("clicked",lambda SLP: self.Encr())
		self.Button_rand.connect("clicked", lambda DR: self.Random())
		self.bbox.add(self.button)
		self.bbox.add(self.Button_rand)
		self.button.set_flags(gtk.CAN_DEFAULT)
		self.button.grab_default()
		self.MainDialog.show_all()
		


	def Encr(self):
		"""
		Данная функция кодирует текст.
		"""

		self.TextIn = self.In.get_text()
		self.plain_text = self.TextIn
		self.encrypted_text = ""
		for self.c in self.plain_text:
			if ord(self.c) % 2 == 1:
			    self.x = ord(self.c)
			    self.x = self.x + 5   # Вы можете изменить данное число на другое.
			    self.c2 = chr(self.x)
			    self.encrypted_text = self.encrypted_text + self.c2
			elif ord(self.c) % 3 == 0:
				self.x = ord(self.c)
				self.x = self.x + 17	# Вы можете изменить данное число на другое.
				self.c2 = chr(self.x)
				self.encrypted_text = self.encrypted_text + self.c2
			elif ord(self.c) % 5 == 0 and ord(self.c) % 2 == 0:
				self.x = ord(self.c)
				self.x = self.x + 80	# Вы можете изменить данное число на другое.
				self.c2 = chr(self.x)
				self.encrypted_text = self.encrypted_text + self.c2
			elif ord(self.c) % 2 == 0:
				self.x = ord(self.c)
				self.x = self.x + 47	# Вы можете изменить данное число на другое.
				encrypted_text = self.encrypted_text + self.c2
		self.Out.set_text(self.encrypted_text)

		self.CreateFolderAndFile()


	def CreateFolderAndFile(self):
		self.File = open('Encrypted text' + '.txt', "a")
		self.File.write(self.Out.get_text())
		self.File.close()

	def Random(self):
		"""
		Данна функция генерирует случайное число
		"""
		self.rand = random.randint(1,5)
		self.Out_In.set_text(str(self.rand))

		self.File = open('Random' + '.txt', "a")
		self.File.write(self.Out_In.get_text() + '\n')
		self.File.close()


def main():
	"""
	Инициализация базового класса и модуля gtk
	"""
	Application = Window()
	gtk.main()


if __name__ == "__main__":
	main()
