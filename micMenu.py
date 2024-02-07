import tkinter as tk
import tkinter.ttk as ttk
import sounddevice as sd

class MicWindow(tk.Toplevel):

	def __init__(self, master = None):
		super().__init__(master = master)
		self.geometry("300x300")
		self.title("Configure Microphone")
		content = ttk.Frame(self, borderwidth = 3, relief="raised")

		deviceList = []
		for x in sd.query_devices():
			deviceList.append(x.get('name'))

		micList = ttk.Combobox(content, text="Choose an input", width=30, values = deviceList)
		cancelButton = ttk.Button(content, text="cancel", command=None)
		acceptButton = ttk.Button(content, text="Accept", command=None)
		print(deviceList)

		content.grid(sticky="news", column=0, row=0)
		micList.grid(column=0, row=0, columnspan=2)
		cancelButton.grid(sticky="sw", column=0, row=1)
		acceptButton.grid(sticky="se", column=1, row=1)

