import tkinter as tk
from tkinter import filedialog


class FileLogger:
	def __init__(self,master,textwidget):
		self.textwidget = textwidget
		self.master = master
		self.filesave = None
		self.fileopen = None
		self.file_title = tk.StringVar()
		self.file_title.set('<Untitled>')
		self.editor_title = ' - Flotex'
		self.master.title(self.file_title.get()+self.editor_title)


	def new_file(self):
		catch = self.textwidget.get(1.0,tk.END)
		if catch != None or catch != '':

			if self.filesave:
				self.textwidget.create_new_file()
				self.master.highlighter.force_highlight()
				self.master.line_number.force_update_line()
				
				self.textwidget = self.textwidget
				self.file_title.set('<Untitled> '+self.editor_title)
				self.master.title(self.file_title.get())
			else:
				
				self.filesave = filedialog.asksaveasfilename(filetypes=[('python file',('*.py','*.pyw'))])
				
				self.textwidget.create_new_file()
				self.master.highlighter.force_highlight()
				self.master.line_number.force_update_line()

				self.textwidget = self.textwidget
				self.file_title.set('<Untitled> '+self.editor_title)
				self.master.title(self.file_title.get())
		else:
			self.textwidget.create_new_file()
			self.master.highlighter.force_highlight()
			self.master.line_number.force_update_line()

			self.textwidget = self.textwidget
			self.file_title.set('<Untitled> '+self.editor_title)
			self.master.title(self.file_title.get())


	def open_file(self):
		''' to open files from computer directory'''
		self.fileopen = filedialog.askopenfilename(filetypes=[('python file',('*.py','*.pyw'))])
		if self.fileopen:
			self.textwidget.display_file_content(self.fileopen)
			self.file_title.set(str(self.fileopen)+self.editor_title)
			self.master.title(self.file_title.get())
			self.master.line_number.force_update_line()
			self.master.highlighter.force_highlight()
			#self.master.line_number.yview_moveto()

	def save_as_file(self):
		''' to open the save as dirctory'''
		self.filesave = filedialog.asksaveasfilename(filetypes=[('python file',('*.py','*.pyw'))])
		if self.filesave:
			self.textwidget.saveas = True
			contents = self.textwidget.get(1.0,tk.END)
			with open(self.filesave,'w') as file:
				file.write(contents)
			self.file_title.set(str(self.filesave)+self.editor_title)
			self.master.title(self.file_title.get())
		else:
			self.file_title.set(str(self.filesave)+self.editor_title)
			self.master.title(self.file_title.get())


	def save_file(self):
		if not self.filesave:
			self.filesave = self.fileopen if self.fileopen else None
			if not self.filesave:
				self.filesave = filedialog.asksaveasfilename(filetypes=[('python file',('*.py','*.pyw'))])

				

		if self.filesave:
			contents = self.textwidget.get(1.0,tk.END)
			with open(self.filesave,'w') as file:
				file.write(contents)
			self.file_title.set(str(self.filesave)+self.editor_title)
			self.master.title(self.file_title.get())



