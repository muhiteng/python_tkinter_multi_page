
# Python Tkinter GUI Application With Multiple Pages | Switch Pages in Tkinter | Tkinter Pagination

import tkinter as tk

class My_App(tk.Frame):

    def __init__(self,root): 
        self.color1='#222448'
        self.color2='#54527E'
        self.color3='WHITE'

        super().__init__(root,bg=self.color1 )

        self.main_frame=self
        self.main_frame.pack(fill=tk.BOTH,expand=True)
        self.main_frame.columnconfigure(0,weight=1)
        self.main_frame.rowconfigure(0,weight=1)


if __name__ == "__main__":
    root = tk.Tk()

    root.title='Multi page app'
    root.geometry('700x500')
    root.resizable(width=False,height=False)

    app=My_App(root)
    root.mainloop()