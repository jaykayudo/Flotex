import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import families


class FontChooser(tk.Toplevel):
	def __init__(self,master,**kwargs):
		super().__init__(**kwargs)
		self.master = master
		self.transient(self.master) # u can only access the self.master widget after closing this widget
		self.title('Choose Font and Font Size')
		self.geometry('500x250')

		self.choose_font_text = tk.Label(self,text='Choose Font')
		self.choose_font_size_text = tk.Label(self,text='Choose Font Size ')
		self.font_list = tk.Listbox(self,exportselection= True)
		self.font_list_scroller = ttk.Scrollbar(self,orient='vertical',command=self.scroll_list)
		self.font_list.configure(yscrollcommand = self.font_list_scroller.set)

		self.available_fonts = sorted(families())
		#print(self.available_fonts)
		for family in self.available_fonts:
			self.font_list.insert(tk.END,family)

		

		current_selection_index = self.available_fonts.index(self.master.font_family)
		if current_selection_index:
			self.font_list.select_set(current_selection_index)# tags the elements at the provided index without changing the currently
			#selected item

			self.font_list.see(current_selection_index)# moves your view to the particularly provided index

		font_size = 14
		self.size_input = tk.Spinbox(self,from_= 5,to=99,value=self.master.font_size,increment=1,format='%1.0f')
		self.save_button = ttk.Button(self,text='Save',command=self.save) 

		self.save_button.pack(side='bottom',pady=(10,0))
		self.choose_font_text.pack(side='left')
		self.font_list.pack(side='left',fill='y')
		self.font_list_scroller.pack(side='left',fill='y',padx=(0,20))
		self.choose_font_size_text.pack(side='left',padx=(0,5))
		self.size_input.pack(side='left',fill='x')

	
		




	def save(self):
		selected_item = self.font_list.curselection()[0]
		font_family = self.font_list.get(selected_item)
		font_size = self.size_input.get()
		yaml_file_content = f"family: {font_family}\n" \
							+ f"size: {font_size}"

		#note : always put a space betweeen keywords and values in writing yaml files
		with open('fonts/font.yaml','w') as file:
			file.write(yaml_file_content)

		self.master.update_font()

	def scroll_list(self,*args):
		if len(args) > 1:
			self.font_list.yview_moveto(args[1])
			
		else:
			event = args[0]
			if event.delta:
				move = -1*(event.delta/120)
			else:
				if event.num == 5:
					move = 1
				else:
					move = -1
			self.font_list.yview_scroll(int(move),'units')

