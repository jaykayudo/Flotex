import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox

class FindWindow(tk.Toplevel):
	def __init__(self,master,**kwargs):
		super().__init__(kwargs)
		self.master = master
		self.geometry('350x150')
		self.title("Find and Replace")
		self.resizable(False,False)
		self.transient(self.master)

		self.style = ttk.Style()
		self.style.configure('TEntry',foreground='black')

		self.top_frame = tk.Frame(self,bg="black",width=350,height=50)
		self.top_frame.pack_propagate(0)

		self.middle_frame = tk.Frame(self,bg="black",width=350,height=50)
		self.middle_frame.pack_propagate(0)

		self.bottom_frame = tk.Frame(self,bg="black",width=350,height=50)
		self.bottom_frame.pack_propagate(0)

		self.text_to_find = tk.StringVar()
		self.replace_text = tk.StringVar()

		self.find_entry_text = tk.Label(self.top_frame,text="Find:",fg="white",bg='black',font=(None,15))
		self.find_entry = ttk.Entry(self.top_frame,textvar = self.text_to_find,width=45,style='TEntry')

		self.replace_entry_text = tk.Label(self.middle_frame,text="Replace:",fg="white",bg="black",font=(None,15))
		self.replace_entry = ttk.Entry(self.middle_frame,textvar = self.replace_text,width=40,style='TEntry')

		self.style2 = ttk.Style()
		self.style2.configure("TButton",foreground='green',background='green')

		self.find_button = ttk.Button(self.bottom_frame,text='Find',command=self.on_find,style='TButton')
		self.replace_button = ttk.Button(self.bottom_frame,text='Replace',command = self.on_replace,style="TButton")
		self.cancel_button = ttk.Button(self.bottom_frame,text='Cancel',command=self.master.find_cancel,style='TButton')

		self.top_frame.pack(side="top",fill="x")
		self.middle_frame.pack(side="top",fill="x")
		self.bottom_frame.pack(side=tk.BOTTOM,fill=tk.X)

		self.find_entry_text.pack(side=tk.LEFT,padx=(10,0))
		self.find_entry.pack(side='left')

		self.replace_entry_text.pack(side=tk.LEFT,padx=(10,0))
		self.replace_entry.pack(side='left')

		self.find_button.pack(side='left',padx=(20,20))
		self.replace_button.pack(side='left',padx=(20,20))
		self.cancel_button.pack(side='left',padx=(20,20))

	def on_find(self):
		if self.text_to_find.get():
			self.master.find(self.text_to_find.get())
		else:
			msgbox.showerror('flotex find','invalid characters to be found')

	def on_replace(self):
		if self.text_to_find.get():
			self.master.replace(self.text_to_find.get(),self.replace_text.get())
		else:
			msgbox.showerror('flotex find','No replacement text found')






