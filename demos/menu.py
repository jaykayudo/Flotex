import tkinter as tk


window = tk.Tk()

#main menu widget
menu = tk.Menu(window)

menu.add_command(label='Change Label Text',command = lambda: lab.configure(text='changing text'))
menu.add_command(label='Change Window Size',command=lambda: window.geometry('800x600'))


# creating the submenu
#cascades are menus with sub menus
cascade =  tk.Menu(window)
cascade.add_command(label='Change Label Color',command = lambda: lab.configure(fg='blue'))
cascade.add_command(label='Change Label Highlight',command = lambda: lab.configure(bg='green'))

#cascades should be added to the main menu widget
menu.add_cascade(label='Label Color',menu=cascade)


#creating a context menu i.e the menu that appear when the mouse is right-clicked
context_menu = tk.Menu(window)
context_menu.add_command(label='Close',command= window.destroy)

def on_right_click(event):
	x = window.winfo_x()+event.x
	y = window.winfo_y()+event.y

	context_menu.post(x,y)

window.bind('<Button-3>',on_right_click)

lab = tk.Label(window,text='Change me ')
lab.pack(padx=200,pady=200)
window.configure(menu=menu)

window.mainloop()