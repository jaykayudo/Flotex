import tkinter as tk


class ThemeChanger:
	def __init__(self,master):
		self.master = master

	def light_mode(self):
		white ='white'
		black = 'black'
		self.master.textarea.configure(fg='black',bg='white')
		yaml_file_contents = f"background: '{white}'\n" \
                             + f"foreground: '{black}'\n" \
                             + f"text_background: '{white}'\n" \
                             + f"text_foreground: '{black}'\n"

		with open("schemes/default.yaml", "w") as yaml_file:
			yaml_file.write(yaml_file_contents)
	def dark_mode(self):
		white ='white'
		black = 'black'
		self.master.textarea.configure(fg='white',bg='black')
		yaml_file_contents = f"background: '{black}'\n" \
                             + f"foreground: '{white}'\n" \
                             + f"text_background: '{black}'\n" \
                             + f"text_foreground: '{white}'\n"
		
		with open("schemes/default.yaml", "w") as yaml_file:
			yaml_file.write(yaml_file_contents)

