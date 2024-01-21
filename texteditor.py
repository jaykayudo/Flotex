import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox

import yaml
import time

# created modules import
from textarea import TextArea
from findwindow import FindWindow
from linenumber import Linenumber
from flomenu import FloMenu
from fontchooser import FontChooser
from colorchoice import colorChooser

class MainWindow(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Flotex")
		self.geometry('900x600-30+30')

		self.textarea = TextArea(self,bg="white",fg="black",undo=True,tabs=('1c'))

		self.scrollbar = ttk.Scrollbar(orient='vertical',command=self.scroll_text)

		self.textarea.configure(yscrollcommand = self.scrollbar.set)
		self.line_number = Linenumber(self,self.textarea,width=2,bg='grey',fg='white')


		self.stat_bar = True
		self.menu = FloMenu(self,self.textarea,bg='grey',fg='white',tearoff = 0)
		#tearoff prevent the  menu from been dragged out

		# menu popup dialog when u right click
		self.context_menu = tk.Menu(self,tearoff=0)
		self.context_menu_commands()
		

		# bottom of the text editor where the cursor position is written
		self.current_index = tk.StringVar()
		self.status_bar = tk.Label(self,textvar=self.current_index,bg='grey',fg='white')

		self.font_size = 15
		self.font_family = 'Bell MT'
		self.update_font()
		
		self.foreground = 'black'
		self.background = 'lightgrey'
		self.text_foreground = 'black'
		self.text_background='white'
		self.update_theme()


		# displaying and positioning of all the widgets on the window
		self.status_bar.pack(side='bottom',fill='x')
		self.line_number.pack(side=tk.LEFT,fill="y")
		self.textarea.pack(side="left",fill=tk.BOTH,expand = 1)
		self.scrollbar.pack(side = tk.LEFT,fill=tk.BOTH,expand=0)

		self.highlighter = Highlighter(self.textarea)
		#print(self.textarea.cget('tabs'))
		#while True:
		self.configure(menu=self.menu)
		
		self.bind_event()

	def scroll_text(self,*args):
		if len(args) > 1:
			self.line_number.yview_moveto(args[1])
			self.textarea.yview_moveto(args[1])
		else:
			event = args[0]
			if event.delta:
				move = -1*(event.delta/120)
			else:
				if event.num == 5:
					move = 1
				else:
					move = -1
			self.line_number.yview_scroll(int(move),'units')
			self.textarea.yview_scroll(int(move),'units')
	def find_and_replace(self,event):
		self.find_win()
		return 'break'# to prevent the default action of our chosen keyboard shortcut

	def find_win(self):
		self.findwindow = FindWindow(self)
	def context_menu_commands(self):
		self.context_menu.add_command(label='Cut',command = self.edit_cut)
		self.context_menu.add_command(label='Copy',command = self.edit_copy)
		self.context_menu.add_command(label='Paste',command = self.edit_paste)
		
		self.context_menu.add_separator()
		self.context_menu.add_command(label='Select All',command = self.edit_select_all)


	def new_file(self):
		self.textarea.delete(1.0,tk.END)
		self.textarea = TextArea(self,bg="white",fg="black",undo=True)
		self.highlighter.force_highlight()
		self.line_number.force_update_line()
	def bind_event(self):
		self.bind('<MouseWheel>',self.scroll_text)
		self.bind('<Button-4>',self.scroll_text)
		self.bind('<Button-5>',self.scroll_text)
		self.bind('<Control-f>',self.find_and_replace)
		self.bind('<KeyRelease>',self.key_release_event)
		self.bind('<Button-3>',self.on_right_click)
		self.bind('<Control-s>',self.on_ctrl_s)
		self.bind('<Control-o>',self.on_ctrl_o)
		self.bind('<Control-n>',self.on_ctrl_n)
		self.bind('Alt-F4',self.on_alt_f4,'')
		self.bind('<Control-l>',self.on_ctrl_l)
		

		self.bind('<Button-1>',self.on_left_click,'+')
		# the '+' option means that it should add this event function to any other event function provided
		# i.e button-1 can carry more than one event func attached to it 

	def on_right_click(self,event):
		x = self.winfo_x()+event.x+20 # winfo_x() returns the position of the top left pixel of the window
		y = self.winfo_y()+event.y+20

		self.context_menu.post(x,y)# creates a menu at the position provide
	def on_left_click(self,event):
		self.update_cursor_index()

	def on_alt_f4(self,event):
		self.exit()
		return 'break'
		

	def key_release_event(self,event):
		self.update_cursor_index()

	def on_ctrl_l(self,event):
		self.change_font()
	def change_font(self):
		FontChooser(self)
			
	def update_cursor_index(self):
		self.textarea.tag_remove('findtext',1.0,tk.END)
		cursor_position = self.textarea.index(tk.INSERT)#return the index of the cursor which is been provided by the tk.INSERT opt
		#print(cursor_position)#print the cursor position index by the format 1.0 where 1 is the line number and 0 is the character no
		cursor_position_pieces = str(cursor_position).split('.')# return a list of the line no and char no
		#print(cursor_position_pieces)prints the list out
		cursor_line = cursor_position_pieces[0]#the line number
		cursor_char = cursor_position_pieces[1]# the charcter number

		self.current_index.set('Line '+cursor_line+', Column '+cursor_char)
		#almost the same as sublime text own

	def update_font(self):
		self.load_font_file('fonts/font.yaml')

		self.textarea.configure(font=(self.font_family,self.font_size))
		self.line_number.configure(font=(None,self.font_size))

	def update_theme(self):
		self.load_scheme_file('schemes/default.yaml')

		self.textarea.configure(fg=self.text_foreground,bg=self.text_background)

	def load_font_file(self,file_path):
		with open(file_path,'r') as stream:
			try:
				config = yaml.safe_load(stream)
			except yaml.YAMLError as error:
				print(error)
				return

		self.font_family = config['family']
		self.font_size = config['size']

	def load_scheme_file(self, scheme):
		with open(scheme, 'r') as stream:
			try:
				config = yaml.safe_load(stream)
			except yaml.YAMLError as error:
				print(error)
				return

		self.foreground = config['foreground']
		self.background = config['background']
		self.text_foreground = config['text_foreground']
		self.text_background = config['text_background']

	def on_ctrl_o(self,event):
		self.menu.filelogger.open_file()
	def on_ctrl_s(self,event):
		self.menu.filelogger.save_file()
		if self.menu.filelogger.filesave:
			self.current_index.set(self.current_index.get()+';Saved'+self.menu.filelogger.file_title.get())
			#time.sleep(2)
			self.after(2000,self.update_cursor_index)

	def on_ctrl_n(self,event):
		self.menu.filelogger.new_file()
	def find(self,text):
		count = tk.StringVar()
		self.textarea.tag_configure('findtext',background='green')
		start = 1.0
		if text:
			text = text
			# the [^A-Za-z] is a regex expression thet means that it should tag the word if it does not have any other character
			# attached to it. i.e if we are searching for python, it should not tag wpython
			idx = self.textarea.search(text,start,stopindex=tk.END,count=count)
			# the count set the length of the word searched for and the regexp is enabled to deal also with regex
			self.textarea.see(idx)
			while idx:
				tag_begin = idx
				tag_end = f'{idx}+{count.get()}c'
				self.textarea.tag_add('findtext',tag_begin,tag_end)

				start = tag_end
				idx = self.textarea.search(text,start,stopindex=tk.END,count=count)
		

	def replace(self,textfound,replacetext):
		count = tk.StringVar()
		start = 1.0
		if textfound:
			idx = self.textarea.search(textfound,start,stopindex=tk.END,count=count)

			while idx:
				end = f'{idx}+{count.get()}c'
				self.textarea.replace(idx,end,replacetext)

				start = end
				idx = self.textarea.search(textfound,start,stopindex=tk.END,count=count)
	def find_cancel(self):
		#self.textarea.tag_delete('findtext')
		self.findwindow.destroy()
	def status_bar_toggle(self):
		if self.stat_bar:
			self.status_bar.pack_forget()
			self.stat_bar = False
		else:
			self.line_number.pack_forget()
			self.textarea.pack_forget()
			self.scrollbar.pack_forget()
			self.status_bar.pack(side='bottom',fill='x')
			self.line_number.pack(side=tk.LEFT,fill="y")
			self.textarea.pack(side="left",fill=tk.BOTH,expand = 1)
			self.scrollbar.pack(side = tk.LEFT,fill=tk.BOTH,expand=0)
			self.stat_bar = True
	def tab_movement(self,event):
		cursor = self.textarea.index(tk.INSERT)
		self.textarea.insert(cursor,'    ')
		self.textarea.mark_set(tk.INSERT,cursor+'+4c')
		return 'break'

	def show_about(self):
		msgbox.showinfo('About Flotex','Flotex was created by Joshua Udo as a practical python editor')

	def custom_theme(self):
		colorChooser(self)
	def apply_color_scheme(self, foreground, background, text_foreground, text_background):
		self.textarea.configure(fg=text_foreground, bg=text_background)
		self.background = background
		self.foreground = foreground
		for menu in self.all_menus:
			menu.configure(bg=self.background, fg=self.foreground)
		self.configure_ttk_elements()

	def configure_ttk_elements(self):
		style = ttk.Style()
		style.configure('editor.TLabel', foreground=self.foreground, background=self.background)
		style.configure('editor.TButton', foreground=self.foreground, background=self.background)


	def exit(self):
		if msgbox.askyesno('FLotex Quit',"Do you want to Exit Window ?"):
			self.menu.filelogger.save_file()
			self.after(1000,self.destroy())
	def edit_redo(self):
		self.textarea.event_generate('<Control-y>')
		self.line_number.force_update_line()
		self.highlighter.force_highlight()
	def edit_undo(self):
		self.textarea.event_generate('<Control-z>')
		self.line_number.force_update_line()
		self.highlighter.force_highlight()
	def edit_cut(self):
		self.textarea.event_generate('<Control-x>')
		self.line_number.force_update_line()
	def edit_copy(self):
		self.textarea.event_generate('<Control-c>')
		
	def edit_paste(self):
		self.textarea.event_generate('<Control-v>')
		self.line_number.force_update_line()
		self.highlighter.force_highlight()
	def edit_select_all(self):
		self.textarea.tag_add('sel',1.0,tk.END)



class Highlighter:
	def __init__(self,text_widget):
		self.text_widget = text_widget
		self.numbers_colors = 'blue'
		self.keyword_colors = 'orange'
		self.string_colors = 'gold'
		self.parentheses_colors = 'green'

		self.keyword = ['while','else','if','for','try','except','elif','finally','import','in','as','from','not','and','or','str','int','float']

		self.disallowed_previous_chars = ['-','_','.',]

		self.text_widget.tag_configure('keyword',foreground = self.keyword_colors)
		self.text_widget.tag_configure('number',foreground = self.numbers_colors)
		self.text_widget.tag_configure('string',foreground = self.string_colors)
		self.text_widget.tag_configure('parentheses',foreground = self.parentheses_colors)

		self.text_widget.bind('<KeyRelease>',self.on_key_release)


	def on_key_release(self,event):
		self.highlight()


	def highlight(self):

		length = tk.IntVar()
		start = 1.0
		for keyword in self.keyword:
			keyword = keyword+'[^A-Za-z_-]'
			idx = self.text_widget.search(keyword,start,stopindex=tk.END,count=length,regexp=1)
			while idx:
				char_match_found = int(str(idx).split('.')[1])
				line_match_found = int(str(idx).split('.')[0])

				if char_match_found > 0:
					previous_char_index = str(line_match_found)+'.'+str(char_match_found-1)

					previous_char = self.text_widget.get(previous_char_index,previous_char_index+'+1c')

					if previous_char.isalnum() or previous_char in self.disallowed_previous_chars:
						end = f'{idx}+{length.get()-1}c'
						start = end
						idx = self.text_widget.search(keyword,start,stopindex=tk.END,count=length,regexp=1)
					else:
						end = f'{idx}+{length.get()-1}c'

						self.text_widget.tag_add('keyword',idx,end)
						start = end
						idx = self.text_widget.search(keyword,start,stopindex=tk.END,count=length,regexp=1)
				else:
						end = f'{idx}+{length.get()-1}c'

						self.text_widget.tag_add('keyword',idx,end)
						start = end
						idx = self.text_widget.search(keyword,start,stopindex=tk.END,count=length,regexp=1)
		

		start = 1.0
		idx = self.text_widget.search(r"(\d)+[.]?(\d)*",start,stopindex =tk.END,count=length,regexp=1)
		# the regular expression used here can be broken as follows:
		#(\d)+; match one or more numbers
		#[.?]: match zero or one decimal point
		#(\d): match one or more numbers after the decimal point
		# visit pythex .com for more info on regex
		while idx:
			char_match_found = int(str(idx).split('.')[1])
			line_match_found = int(str(idx).split('.')[0])

			if char_match_found > 0:
				previous_char_index = str(line_match_found)+'.'+str(char_match_found-1)

				previous_char = self.text_widget.get(previous_char_index,previous_char_index+'+1c')

				if previous_char.isalnum() or previous_char in self.disallowed_previous_chars:
					end = f'{idx}+{length.get()}c'
					start = end
					idx = self.text_widget.search(r"(\d)+[.]?(\d)*",start,stopindex =tk.END,count=length,regexp=1)
				else:
					end = f'{idx}+{length.get()}c'

					self.text_widget.tag_add('number',idx,end)
					start = end
					idx = self.text_widget.search(r"(\d)+[.]?(\d)*",start,stopindex =tk.END,count=length,regexp=1)
			else:
					end = f'{idx}+{length.get()}c'

					self.text_widget.tag_add('number',idx,end)
					start = end
					idx = self.text_widget.search(r"(\d)+[.]?(\d)*",start,stopindex =tk.END,count=length,regexp=1)

		self.highlight_regex(r'[\'][^\']*[\']','string')
		#the regex above can be broken down as:
		#[\']:Match the string opening character(')
		#[^\']*: Match any number of character which are not the string-closing character
		#[\']:  Match the string closing character(')

		# same applies to the regex below
		self.highlight_regex(r'[\"][^\']*[\"]','string')

		self.highlight_regex(r'[a-z]+\(\)','parentheses',2)
	def highlight_regex(self,regex,tag,remove = 0):
		length = tk.IntVar()
		start = 1.0
		idx = self.text_widget.search(regex,start,stopindex=tk.END,count=length,regexp=1)
		while idx:
			end = f'{idx}+{length.get()-remove}c'
			self.text_widget.tag_add(tag,idx,end)
			start = end

			idx = self.text_widget.search(regex,start,stopindex=tk.END,count=length,regexp=1)
	def force_highlight(self):
		self.highlight()




if __name__ == "__main__":
	mainwindow = MainWindow()
	mainwindow.mainloop()


