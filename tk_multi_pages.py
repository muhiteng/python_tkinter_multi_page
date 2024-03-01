
# Python Tkinter GUI Application With Multiple Pages | Switch Pages in Tkinter | Tkinter Pagination

import tkinter as tk

class My_App(tk.Frame):

    def __init__(self,root): 
        self.current_page_index=0
        self.pages=[self.page1,self.page2,self.page3,self.page4]   # values is function names

        # self.pages[0]()
        # my_function=self.pages[0]()
        # my_function()

        self.color1='#222448'
        self.color2='#54527E'
        self.color3='WHITE'

        super().__init__(root,bg=self.color1 )

        self.main_frame=self
        
        self.main_frame.pack(fill=tk.BOTH,expand=True)
        self.main_frame.columnconfigure(0,weight=1)
        self.main_frame.rowconfigure(0,weight=1)

        self.load_main_widgets()
    
    def load_main_widgets(self):
        self.create_page_container()
        self.create_pager()
        self.pages[self.current_page_index]()

    def clear_frame(self,frame):
        for child in frame.winfo_children():
            child.destroy()

    def create_page_container(self):
        self.page_container=tk.Frame(
            self.main_frame,
            background=self.color1
        )

        self.page_container.columnconfigure(0,weight=1)
        self.page_container.rowconfigure(0,weight=1)

        self.page_container.grid(column=0,row=0,sticky=tk.NSEW)

    def create_pager(self):
        self.pager=tk.Frame(
            self.main_frame,
            background=self.color1,
            height=125,
            width=500
        )

        self.pager.columnconfigure(1,weight=1)
        self.pager.rowconfigure(0,weight=1)

        self.pager.grid(column=0,row=1,sticky=tk.NS)
        self.pager.grid_propagate(0)

        def change_page(button):
            self.clear_frame(self.page_container)

            match button :
                case 'Previous':
                    self.current_page_index -=1
                    self.pages[self.current_page_index]()
                case 'Next':
                    self.current_page_index +=1
                    self.pages[self.current_page_index]()

            if self.current_page_index ==0 :
                prev_button.config(state=tk.DISABLED) 
            else:
                prev_button.config(state=tk.ACTIVE) 

            if self.current_page_index ==len(self.pages)-1 :
                next_button.config(state=tk.DISABLED) 
            else:
                next_button.config(state=tk.ACTIVE)       

            self.page_number['text']= f'{self.current_page_index+1}/{len(self.pages)}'
        

        prev_button=tk.Button(
            self.pager,
            background=self.color2,
            foreground=self.color3,
            activebackground=self.color2,
            activeforeground=self.color3,
            disabledforeground='#3B3A56',
            highlightthickness=0,
            width=7,
            relief=tk.FLAT,
            font=('Arial',18),
            cursor='hand1',
            text='Previous',
            state=tk.DISABLED,
            command=lambda button='Previous':change_page(button)
        )
        prev_button.grid(column=0,row=0)

        self.page_number=tk.Label(
            self.pager,
            background=self.color1,
            foreground=self.color3,
            font=('Arial',18),
            text=f'{self.current_page_index+1}/{len(self.pages)}'

        )
        self.page_number.grid(column=1,row=0)

        next_button=tk.Button(
            self.pager,
            background=self.color2,
            foreground=self.color3,
            activebackground=self.color2,
            activeforeground=self.color3,
            disabledforeground='#3B3A56',
            highlightthickness=0,
            width=7,
            relief=tk.FLAT,
            font=('Arial',18),
            cursor='hand1',
            text='Next',
             command=lambda button='Next':change_page(button)
           
        )
        next_button.grid(column=2,row=0)


    def create_something(self):
        pass

    def page1(self):
        title=tk.Label(
            self.page_container,
            foreground=self.color3,
            background=self.color1,
            height=2,
            font=('Arial',26,'bold'),
            text='Page 1'
        )
        title.grid(column=0,row=0)

        text=('hello text for page 1' 
              'LOREM IPSUM GENERATOR'
              'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut'
              ' labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
              'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
              'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat'
              ' non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
        
        content=tk.Label(
             self.page_container,
            foreground=self.color2,
            background=self.color3,
            justify=tk.LEFT,
            anchor=tk.N,
            pady=20,
            font=('Arial',16),
            text=text,
            wraplength=600
        )
        content.grid(column=0,row=1,sticky=tk.NSEW)

    def page2(self):
        title=tk.Label(
            self.page_container,
            foreground=self.color3,
            background=self.color1,
            height=2,
            font=('Arial',26,'bold'),
            text='Page 2'
        )
        title.grid(column=0,row=0)

        text=('hello text for page 2' 
              'LOREM IPSUM GENERATOR'
              'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut'
              ' labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
              'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
              'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat'
              ' non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
        
        content=tk.Label(
             self.page_container,
            foreground=self.color2,
            background=self.color3,
            justify=tk.LEFT,
            anchor=tk.N,
            pady=20,
            font=('Arial',16),
            text=text,
            wraplength=600
        )
        content.grid(column=0,row=1,sticky=tk.NSEW)

    def page3(self):
        title=tk.Label(
            self.page_container,
            foreground=self.color3,
            background=self.color1,
            height=2,
            font=('Arial',26,'bold'),
            text='Page 3'
        )
        title.grid(column=0,row=0)

        text=('hello text for page 3' 
              'LOREM IPSUM GENERATOR'
              'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut'
              ' labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
              'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
              'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat'
              ' non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
        
        content=tk.Label(
             self.page_container,
            foreground=self.color2,
            background=self.color3,
            justify=tk.LEFT,
            anchor=tk.N,
            pady=20,
            font=('Arial',16),
            text=text,
            wraplength=600
        )
        content.grid(column=0,row=1,sticky=tk.NSEW)

    def page4(self):
        title=tk.Label(
            self.page_container,
            foreground=self.color3,
            background=self.color1,
            height=2,
            font=('Arial',26,'bold'),
            text='Page 4'
        )
        title.grid(column=0,row=0)

        text=('hello text for page 4' 
              'LOREM IPSUM GENERATOR'
              'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut'
              ' labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
              'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
              'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat'
              ' non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
        
        content=tk.Label(
             self.page_container,
            foreground=self.color2,
            background=self.color3,
            justify=tk.LEFT,
            anchor=tk.N,
            pady=20,
            font=('Arial',16),
            text=text,
            wraplength=600
        )
        content.grid(column=0,row=1,sticky=tk.NSEW)



if __name__ == "__main__":
    root = tk.Tk()

    root.title('Multi page app')
    root.geometry('700x500')
    root.resizable(width=False,height=False)

    app=My_App(root)
    root.mainloop()