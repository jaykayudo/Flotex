import tkinter as tk

class Tag(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Tags")
		self.text = tk.Text(self)
		self.text.pack(side=tk.TOP,fill='y')
		
		self.text.bind('<Control-f>',self.configuring_tags,'')# the empty string option means that the function should replace any other binding of the same shorcut key

		self.text.bind('<Control-r>',self.raise_selected)
		self.text.bind('<Control-u>',self.underline_selected)
		self.text.bind('<Control-d>',self.duplicate_text)

		self.text.bind('<KeyRelease>',self.search_word)
		

	def configuring_tags(self,event = None):
		lineend = self.text.index(tk.INSERT)
		lineend = lineend.split('.')
		lineend = int(lineend[1])
		for i in range(lineend):
			index = '1.'+str(i)
			end= '1.end'
			self.text.tag_add('even',index,end)# args are: call tag,start_point of the tag, end point of the tag
		self.text.tag_configure('even',foreground= 'green')# args are: create tag,what the tag should affect 

	def raise_selected(self,event=None):
		
		selected_pos = self.text.tag_ranges('sel')# the range of the selection u made. returns a list of elements: starting index and ending index of the selected area

		try:
			self.text.tag_add('raise',selected_pos[0],selected_pos[1])
		except:#to prevent an error incase there is no selected area
			pass 
		self.text.tag_configure('raise',offset=5)# the offset raises the selected text

		return 'break' # overwrites any default event of the selected shorcut key
	def underline_selected(self,event=None):
		self.text.tag_configure('underline',underline=1)
		selected_pos = self.text.tag_ranges('sel')# the range of the selection u made. returns a list of elements: starting index and ending index of the selected area

		try:
			self.text.tag_add('underline',selected_pos[0],selected_pos[1])
		except:
			pass
		

		return 'break' # overwrites any default event of the selected shorcut key

	# duplicating a text
	def duplicate_text(self,event):
		cursor_pos = self.text.index(tk.INSERT)
		cursor_pos = cursor_pos.split('.')
		
		selected_area = self.text.tag_ranges('sel')
		new_pos = str(selected_area[1])
		
		new_pos = new_pos.split('.')
		
		new_pos = str(int(new_pos[0])+1)+'.0'
		

		text_copy = self.text.get(selected_area[0],selected_area[1]) # returns the text within this indexes
		

		self.text.insert(new_pos,'\n'+text_copy)
		return 'break'

	def search_word(self,event):
		self.text.tag_configure('color',foreground='purple')
		start = 1.0
		idx = self.text.search('python',start,stopindex=tk.END)
		while idx:
			tag_begin = idx
			tag_end = f'{idx}+6c'
			self.text.tag_add('color',tag_begin,tag_end)

			start = tag_end
			idx = self.text.search('python',start,stopindex = tk.END)


	
if __name__ == '__main__':
	tag = Tag()
	tag.mainloop()
