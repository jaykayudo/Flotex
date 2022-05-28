import tkinter as tk
from file_logger import FileLogger


class FloMenu(tk.Menu):
	def __init__(self,master,text_widget,**kwargs):
		super().__init__(**kwargs)
		self.master = master
		self.filelogger = FileLogger(master,text_widget)

		self.file_menu = tk.Menu(master)
		self.edit_menu = tk.Menu(master)
		self.lab = tk.Label(master,text='menu')
		self.lab.pack(padx=100,pady=100)

		self.file_commands()
		self.edit_commands()

		self.add_cascade(label='File',menu=self.file_menu)
		self.add_cascade(label='Edit',menu=self.edit_menu)

	def file_commands(self):
		self.file_menu.add_command(label='New File \t\t\t\t  Ctrl+N',command=self.filelogger.new_file)
		self.file_menu.add_command(label='Open File \t\t\t\t Ctrl+O',command=self.filelogger.open_file)
		self.file_menu.add_command(label='Open Folder ',command=lambda: self.lab.config(text='Opening Folder'))
		self.file_menu.add_command(label='Save \t\t\t\t Ctrl+S',command=self.save_file)
		self.file_menu.add_command(label='Save as \t\t\t\t ',command=self.filelogger.save_as_file)
		self.file_menu.add_command(label='Exit \t\t\t\t  Alt+f4',command=self.master.exit)
	def edit_commands(self):
		# self.edit_menu.add_command(label='Undo \t\t\t\t  Ctrl+Z',command=self.)
		# self.edit_menu.add_command(label='R \t\t\t\t Ctrl+O',command=self.filelogger.open_file)
		# self.edit_menu.add_command(label='Open Folder ',command=lambda: self.lab.config(text='Opening Folder'))
		# self.edit_menu.add_command(label='Save \t\t\t\t Ctrl+S',command=lambda: self.lab.config(text='Saving File'))
		# self.edit_menu.add_command(label='Save as \t\t\t\t ',command=self.filelogger.save_as_file)
		# self.edit_menu.add_command(label='Close File \t\t\t\t  Ctrl+w',command=lambda: self.lab.config(text='Closing File'))
		pass

	





# window = tk.Tk()
# window.geometry("800x600")
# flomenu = FloMenu(window)
# window.configure(menu=flomenu)
# window.mainloop()