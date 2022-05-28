import tkinter as tk
import tkinter.ttk as ttk
from file_logger import FileLogger
from findwindow import FindWindow
from themechanger import ThemeChanger


class FloMenu(tk.Menu):
	def __init__(self,master,text_widget,**kwargs):
		super().__init__(**kwargs)
		self.master = master
		self.filelogger = FileLogger(master,text_widget)
		self.view_label = tk.StringVar()
		self.view_label.set("Hide Status Bar")
		
		self.theme_changer = ThemeChanger(master)

		self.file_menu = tk.Menu(master,tearoff=0)
		#tearoff prevent the  menu from been dragged out
		self.edit_menu = tk.Menu(master,tearoff = 0)
		self.view_menu = tk.Menu(master,tearoff=0)
		self.tool_menu = tk.Menu(master,tearoff = 0)
		self.help_menu = tk.Menu(master,tearoff=0)
		
		

		self.file_commands()
		self.edit_commands()
		self.tools_command()
		self.help_command()
		self.view_menu.add_command(label=self.view_label.get(),command = self.view_command)

		self.add_cascade(label='File',menu=self.file_menu)
		self.add_cascade(label='Edit',menu=self.edit_menu)
		self.add_cascade(label='View',menu=self.view_menu)
		self.add_cascade(label='Tools',menu=self.tool_menu)
		
		self.add_cascade(label='Help',menu=self.help_menu)

	def file_commands(self):
		self.file_menu.add_command(label='New File \t\t\t\t  Ctrl+N',command=self.filelogger.new_file)
		self.file_menu.add_command(label='Open File \t\t\t\t Ctrl+O',command=self.filelogger.open_file)
		self.file_menu.add_command(label='Open Folder ',command= self.destroy)
		self.file_menu.add_separator()
		self.file_menu.add_command(label='Save \t\t\t\t Ctrl+S',command=self.filelogger.save_file)

		self.file_menu.add_command(label='Save as \t\t\t\t ',command=self.filelogger.save_as_file)
		self.file_menu.add_separator()
		self.file_menu.add_command(label='Exit \t\t\t\t  Alt+f4',command=self.master.exit)
	def edit_commands(self):
		self.edit_menu.add_command(label='Undo \t\t\t\t  Ctrl+Z',command=self.master.edit_undo)
		self.edit_menu.add_command(label='Redo \t\t\t\t Ctrl+R',command=self.master.edit_redo)
		self.edit_menu.add_separator()
		self.edit_menu.add_command(label='Cut ',command=self.master.edit_cut)
		self.edit_menu.add_command(label='Copy \t\t\t\t Ctrl+c',command=self.master.edit_copy)
		self.edit_menu.add_command(label='Paste \t\t\t\t ',command=self.master.edit_paste)
		self.edit_menu.add_separator()
		self.edit_menu.add_command(label='Select All \t\t\t\t  Ctrl+a',command=self.master.edit_select_all)
		self.edit_menu.add_separator()
		self.edit_menu.add_command(label='Find and Replace    Ctrl+f',command=self.master.find_win)

	def view_command(self):
		
		if self.master.stat_bar:
			self.view_label.set('Show Status bar')
			self.master.status_bar_toggle()
			self.view_menu.delete(index1=0)
			self.view_menu.insert_command(index=0,label=self.view_label.get(),command = self.view_command)
		else:
			self.view_label.set('Hide Status Bar')
			self.master.status_bar_toggle()
			self.view_menu.delete(index1=0)
			self.view_menu.insert_command(index=0,label=self.view_label.get(),command = self.view_command)
		
		


		
	def tools_command(self):
		self.tool_menu.add_command(label='Change Font',command = self.master.change_font)
		self.theme_change = tk.Menu(self,tearoff=False)
		self.tool_menu.add_cascade(label='Change Theme',menu=self.theme_change)
		self.theme_change.add_command(label='Dark Mode',command = self.theme_changer.dark_mode)
		self.theme_change.add_command(label='Light Mode',command = self.theme_changer.light_mode)
		self.theme_change.add_command(label='Customise Theme',command = self.master.custom_theme)

	
	def help_command(self):
		self.help_menu.add_command(label='About',command=self.master.show_about)
	

	





# window = tk.Tk()
# window.geometry("800x600")
# flomenu = FloMenu(window)
# window.configure(menu=flomenu)
# window.mainloop()