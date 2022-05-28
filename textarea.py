import tkinter as tk

class  TextArea(tk.Text):
	def __init__(self,master,**kwargs):
		super().__init__(**kwargs)
		self.bind_events()

		self.master = master
		self.config(wrap = tk.WORD)
		self.saveas = False
		self.saved = False
	def bind_events(self):
		self.bind('<Control-a>',self.select_all)
		self.bind('<Control-c>',self.copy)
		self.bind('<Control-v>',self.paste)
		self.bind('<Control-y>',self.redo)
		self.bind('<Control-z>',self.undo)
		self.bind('<Control-x>',self.cut)
		self.bind('<KeyPress>',self.on_key_press)
		self.bind('<Button-1>',self.update_cursor_index)
		#self.bind('<Tab>',self.tab_movement)
		

	def tab_movement(self,event):
		cursor = self.index(tk.INSERT)
		self.insert(cursor,'    ')
		self.mark_set(tk.INSERT,cursor+'+4c')
		return 'break'



	def move_four_chars(self,event):
		cursor_index = self.index(tk.INSERT)
		self.mark_set(tk.INSERT,cursor_index+'+4c')
		return 'break'
	def cut(self,event):
		self.event_generate('<<Cut>>')
		return 'break'
	def copy(self,event):
		self.event_generate('<<Copy>>')

	def paste(self,event):
		self.event_generate('<<Paste>>')
		return 'break'
	def redo(self,event):
		self.event_generate('<<Redo>>')
		return 'break'
	def undo(self,event):
		self.event_generate('<<Undo>>')
		return 'break'
	def select_all(self,event):
		self.tag_add('sel',1.0,tk.END)
		return 'break'
	def on_key_press(self,**args):
		self.master.line_number.yview_moveto(args[1])
	def update_cursor_index(self,event):
		cursor_position = self.index(tk.INSERT)#return the index of the cursor which is been provided by the tk.INSERT opt
		#print(cursor_position)#print the cursor position index by the format 1.0 where 1 is the line number and 0 is the character no
		cursor_position_pieces = str(cursor_position).split('.')# return a list of the line no and char no
		#print(cursor_position_pieces)prints the list out
		cursor_line = cursor_position_pieces[0]#the line number
		cursor_char = cursor_position_pieces[1]# the charcter number

		self.master.current_index.set('Line '+cursor_line+', Column '+cursor_char)
		#almost the same as sublime text own
	

	def display_file_content(self,file_path):
		with open(file_path,'r') as file:
			

		
			self.delete(1.0,tk.END)
			self.insert(1.0,file.read())

	def create_new_file(self):
		self.master.new_file()



