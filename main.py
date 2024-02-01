import tkinter as tk
import tkinter.ttk as ttk
import sounddevice as sd
from micMenu import MicWindow

# ------------------------------------DEFS----------------------------------- #

def update_val(lbl):
	out = "Current level: {:0.0f}%".format(float(lbl))
	val.config(text = out)

def enable():
	global enabled
	if enabled:
		style.configure("confirm.TLabel", foreground="red")
		enableCheck.config(text="Currently Disabled")
		enabled = False
	else:
		style.configure("confirm.TLabel", foreground="green")
		enableCheck.config(text="Currently Enabled")
		enabled = True

def show_grid():
	global showGrid
	global frameList
	if showGrid:
		for x in frameList:
			x.configure(relief='flat')
		showGrid = False
	else:
		for x in frameList:
			x.configure(relief='raised')
		showGrid = True

def make_framelist():
	global frameList
	frameList.append(content)
	frameList.append(scaleFrame)
	frameList.append(enableButtonFrame)
	frameList.append(enableCheckFrame)
	frameList.append(valFrame)

# ----------------------------------GUI------------------------------------- #

# main window & setup
window = tk.Tk()
style = ttk.Style()
enabled = False
showGrid = False
dbVal = tk.DoubleVar()

#styles
style.configure("confirm.TLabel", foreground="red")
style.configure("enable.TButton")

# menus
window.option_add('*tearOff', False)
menubar = tk.Menu(window)
debugmenu = tk.Menu(menubar, tearoff=0)
debugmenu.add_command(label="Show Grid", command=show_grid)
settingsmenu = tk.Menu(menubar, tearoff=0)
settingsmenu.add_command(label="Configure Microphone", command=lambda: MicWindow(window))
menubar.add_cascade(label="Settings", menu=settingsmenu)
menubar.add_cascade(label="Debug", menu=debugmenu)
window.config(menu=menubar)

# main elements of UI, subject to change
frameList = []

content = ttk.Frame(window, borderwidth=3)
scaleFrame = ttk.Frame(content, borderwidth=3)
enableButtonFrame = ttk.Frame(content, borderwidth=3)
enableCheckFrame = ttk.Frame(content, borderwidth=3)
valFrame = ttk.Frame(content, borderwidth=3)
make_framelist()

scale = ttk.Scale(scaleFrame, orient='vertical', length=200, from_=100, to=1, variable = dbVal, command=update_val)
enableButton = ttk.Button(content, text="Enable", default="active", command=enable, style="enable.TButton")
enableCheck = ttk.Label(enableCheckFrame, text ="Currently Disabled", anchor="n", style="confirm.TLabel")
val = ttk.Label(valFrame, text="Current level: 0%", justify="center")
scale.pack()
enableCheck.pack()
val.pack()


# Grid. Currently 3x2
content.grid(column=0, row=0, sticky="news")
scaleFrame.grid(column=0, row=0, rowspan=2, sticky="news")
enableButton.grid(sticky="s", column=1, row=0)
enableCheckFrame.grid(sticky="news", column=1, row=1)
valFrame.grid(column=0, row=2, sticky="news")

#print(content.winfo_class())
#print(style.layout('TFrame'))

window.mainloop()
