import tkinter as tk


class CursorIndex(tk.Tk):

	def __init__(self):
		super().__init__()
		self.current_index = tk.StringVar()
		self.text = tk.Text(self)
		self.label = tk.Label(self,textvar=self.current_index)
		

		self.text.pack(side='top',fill='x')
		self.label.pack(side='bottom',fill='y')
		self.text.bind('<KeyRelease>',self.update_cursor_index)
		self.text.bind('<Control-d>',self.down_three_lines)
		self.text.bind('<Control-w>',self.highlight_word)
		self.text.bind('<Control-b>',self.back_four_characters)
		self.text.bind('<Control-h>',self.highlight_line)

	def update_cursor_index(self,event):
		cursor_position = self.text.index(tk.INSERT)#return the index of the cursor which is been provided by the tk.INSERT opt
		#print(cursor_position)#print the cursor position index by the format 1.0 where 1 is the line number and 0 is the character no
		cursor_position_pieces = str(cursor_position).split('.')# return a list of the line no and char no
		#print(cursor_position_pieces)prints the list out
		cursor_line = cursor_position_pieces[0]#the line number
		cursor_char = cursor_position_pieces[1]# the charcter number

		self.current_index.set('Line '+cursor_line+', Column '+cursor_char)
		#almost the same as sublime text own
	def down_three_lines(self,event):
		current_index= str(self.index(tk.INSERT))
		newpos = current_index+'+3l'# note: it is 3l not 31
		self.mark_set(tk.INSERT,newpos)
		return 'break'
	def highlight_word(self,event):
		start = self.index(tk.INSERT)+'wordstart'
		end = self.index(tk.INSERT)+'wordend'
		self.tag_add('sel',start,end)
		return 'break'
	def highlight_line(self,event):
		start = self.index(tk.INSERT)+'linestart'
		end = self.index(tk.INSERT)+'lineend'
		self.tag_add('sel',start,end)
		return 'break' # to prevent the default action of our chosen keyboard shortcut
	def back_four_characters(self,event):
		current_index = self.index(tk.INSERT)
		new_pos = str(current_index)+'-4c'# back 4 characters
		self.mark_set(tk.INSERT,new_pos)

if __name__ == "__main__":
	cursor_index = CursorIndex()
	cursor_index.mainloop()

