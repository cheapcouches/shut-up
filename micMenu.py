import tkinter as tk
import tkinter.ttk as ttk
import sounddevice as sd

class MicWindow(tk.Toplevel):

	def __init__(self, master = None):
		super().__init__(master = master)
		self.geometry("300x300")
		self.title("Configure Microphone")
		content = ttk.Frame(self, borderwidth = 3, relief="raised")

		micList = ttk.Combobox(content, text="Choose an input", values = sd.query_devices(kind='input'))
		cancelButton = ttk.Button(content, text="cancel", command=None)
		acceptButton = ttk.Button(content, text="Accept", command=None)

		content.grid(sticky="news", column=0, row=0)
		micList.grid(column=0, row=0, columnspan=2)
		cancelButton.grid(sticky="sw", column=0, row=1)
		acceptButton.grid(sticky="se", column=1, row=1)

