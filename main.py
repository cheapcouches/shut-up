\import tkinter as tk
import tkinter.ttk as ttk

def update_val(lbl):
	out = "Current level: {:0.0f}%".format(float(lbl))
	val.config(text = out)

# main window
window = tk.Tk()

# used for scale later :)
dbVal = tk.DoubleVar()

# main elements of UI, subject to change
content = ttk.Frame(window, width=600, height=400,borderwidth=5)
scale = ttk.Scale(content, orient='vertical', length=200, from_=100, to=1, variable = dbVal, command=update_val)
enable = ttk.Button(content, text="Enable")
val = ttk.Label(content, text="Current level: 0%")

content.grid(column=0, row=0)
scale.grid(column=0, row=0, rowspan=2)
enable.grid(column=1, row=0, rowspan=2)
val.grid(column=0, row=3)

#print(content.winfo_class())
#print(style.layout('TFrame'))

window.mainloop()
