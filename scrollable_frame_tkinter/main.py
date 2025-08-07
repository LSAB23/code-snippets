import tkinter as tk
from tkinter import ttk

# Normal Tkinter
class ScrollFrame(tk.Frame):
	def __init__(self, parent):
		super().__init__(master = parent)
		self.pack(expand = True, fill = 'both')

		self.frame_height = 10

		# canvas 
		self.canvas = tk.Canvas(self,scrollregion = (0,0,self.winfo_width(),self.frame_height))
		self.canvas.pack(expand = True, fill = 'both')

		
		# display frame
		self.frame = ttk.Frame(self)
		

		#scrollbar
		self.scrollbar = ttk.Scrollbar(parent, orient = 'vertical', command = self.canvas.yview)
		self.canvas.configure(yscrollcommand = self.scrollbar.set)
		self.scrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')

		# events
		self.canvas.bind_all('<MouseWheel>', lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"))
		self.bind('<Configure>', self.update_size)

	def update_size(self, event):
		# set the height to the frame width
		self.frame_height = self.frame.winfo_reqheight()
		# set the width so that the scrollbar do no cover the frame widgets
		width = self.winfo_width()-(self.scrollbar.winfo_width()+2)
		
		if self.frame_height >= self.winfo_height():
			height = self.frame_height
			# adding the ability for user to use the mouse wheel to move the scrollbar
			self.canvas.bind_all('<MouseWheel>', lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"))
			self.scrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')
		else:
			# when the height is the same as current window height just remove the scrollbar
			height = self.winfo_height()
			self.canvas.unbind_all('<MouseWheel>')
			self.scrollbar.place_forget()
		
		self.canvas.configure(scrollregion=(0,0,width, height))
		
		self.canvas.create_window(
			(0,0), 
			window = self.frame, 
			anchor = 'nw', 
			width = width, 
			height = height)

# Custom Tkinter
# import customtkinter as ctk
# from tkinter import ttk

# class ScrollFrame(ctk.CTkFrame):
# 	def __init__(self, parent):
# 		super().__init__(master = parent)
# 		self.pack(expand = True, fill = 'both')

# 		self.frame_height = 10

# 		# canvas 
# 		self.canvas = ctk.CTkCanvas(self,scrollregion = (0,0,self.winfo_width(),self.frame_height))
# 		self.canvas.pack(expand = True, fill = 'both')

		
# 		# display frame
# 		self.frame = ctk.CTkFrame(self)
		

# 		#scrollbar
# 		self.scrollbar = ctk.CTkScrollbar(parent, orientation = 'vertical', command = self.canvas.yview)
# 		self.canvas.configure(yscrollcommand = self.scrollbar.set)
# 		self.scrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')

# 		# events
# 		self.canvas.bind_all('<MouseWheel>', lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"))
# 		self.bind('<Configure>', self.update_size)

# 	def update_size(self, event):
# 		# set the height to the frame width
# 		self.frame_height = self.frame.winfo_reqheight()
# 		# set the width so that the scrollbar do no cover the frame widgets
# 		width = self.winfo_width()-(self.scrollbar.winfo_width()+2)
		
# 		if self.frame_height >= self.winfo_height():
# 			height = self.frame_height
# 			# adding the ability for user to use the mouse wheel to move the scrollbar
# 			self.canvas.bind_all('<MouseWheel>', lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"))
# 			self.scrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')
# 		else:
# 			# when the height is the same as current window height just remove the scrollbar
# 			height = self.winfo_height()
# 			self.canvas.unbind_all('<MouseWheel>')
		
# 		self.canvas.configure(scrollregion=(0,0,width, height))
		
# 		self.canvas.create_window(
# 			(0,0), 
# 			window = self.frame, 
# 			anchor = 'nw', 
# 			width = width, 
# 			height = height)
	
if __name__ == '__main__':
	window = tk.Tk()
	window.geometry('600x500')
	window.title('Scrolling')


	scroll_frame = ScrollFrame(window)
	main_frame = scroll_frame.frame

	for i in range(100):
		ttk.Button(main_frame, text=f'This is a button{i}').pack(expand=True, fill='both')

	tk.Button(main_frame, text='This is a button before', height=10).pack(expand=True, fill='both')
	ttk.Button(main_frame, text='This is a button last').pack(expand=True, fill='both')

	window.mainloop()
