import tkinter as tk
class Linenumber(tk.Text):
	def __init__(self,master,textarea,**kwargs):
		super().__init__(**kwargs)
		self.master = master
		self.textarea = textarea
		self.num = 1
		self.insert(1.0,'1')
		self.configure(state="disabled")
		self.textarea.bind('<KeyPress>',self.add_number)
		self.textarea.bind('<Button-1>',self.button1_events)

	def add_number(self,event):
		index  = self.textarea.index(tk.END)
		line_index = str(index).split('.')[0]
		line_num = '\n'.join(str(int(no)+1) for no in range(int(line_index)))
		width = len(line_index)
		self.config(state='normal',width=width)
		self.delete(1.0,tk.END)
		self.insert(1.0,line_num)
		self.config(state='disabled')
		self.highlight_cursor_pos()


	def button1_events(self,event):
		self.highlight_cursor_pos()
	def highlight_cursor_pos(self):
		self.tag_delete('highlight')
		cursor_index = self.textarea.index(tk.INSERT)
		cursor_line_index = str(cursor_index).split('.')[0]
		highlight_start_index = cursor_line_index+'.0' 
		highlight_end_index = highlight_start_index+'lineend'
		self.tag_configure('highlight',background='green')
		self.tag_add('highlight',highlight_start_index,highlight_end_index)



# window = tk.Tk()
# textarea = tk.Text(window)
# linenum = Linenumber(window,textarea,width=1,fg='white',bg='grey')
# linenum.pack(side='left',fill='y')
# textarea.pack(side='left',fill='both')
# window.mainloop()
