import ttkbootstrap as ttk
from PIL import Image, ImageTk
from Dandy_Drinks.Images import RIGHT_DRINK
from Dandy_Drinks.Images import LEFT_DRINK

"""
MainButtonGroup is a class that inherits from the tkinter Frame. It contains a left drink image, a right drink image and
four buttons named Search By Drink Categories, Select Random, Search Alphabetically, and Search By Ingredient. The 
parameter field of the constructor takes several arguments.
1. gif - This is the banner image in the main application window. It is a object.
2. text_area - this is the text section of the main application window. It is a object.
3. destroy_widgets - this is a method that is passed in that will create the random page if called.
4. create_category_page - this is a method that will create the category page if called.
5. create_alphabetical_page - this is a method that will create the alphabetical page if called.
6. create_ingredient_page - this is a method that will create the ingredient page if called.
"""


class MainButtonGroup(ttk.Frame):

    def __init__(self, parent, gif, text_area, destroy_widgets, create_category_page, create_alphabetical_page,
                 create_ingredient_page):
        ttk.Frame.__init__(self, parent)
        self.gif = gif
        self.text_area = text_area
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=1)
        # -----------------------------------LEFT IMAGE-----------------------------------------------------------------
        self.left_image_raw = Image.open(LEFT_DRINK)
        self.image_resize = self.left_image_raw.resize((120, 190), Image.ANTIALIAS)
        self.left_image = ImageTk.PhotoImage(self.image_resize)
        self.left_content = ttk.Label(
            self,
            image=self.left_image
        )
        self.left_content.grid(row=0, column=0, sticky='w')
        # button frame
        self.button_frame = ttk.Frame(self)
        self.button_frame.grid(row=0, column=1)
        # ----------------------------------------------------BUTTONS---------------------------------------------------
        self.button1 = ttk.Button(
            self.button_frame,
            text="Search By Drink Categories",
            bootstyle="info",
            width=30,
            command=create_category_page
        )
        self.button1.grid(row=0, column=0, padx=(0, 20), pady=(0, 10), ipadx=15, ipady=10)

        # button 2
        self.button2 = ttk.Button(
            self.button_frame,
            text="Select Random",
            bootstyle="info",
            width=30,
            command=destroy_widgets
        )
        self.button2.grid(row=0, column=1, padx=20, pady=(0, 10), ipadx=15, ipady=10)

        # button 3
        self.button3 = ttk.Button(
            self.button_frame,
            text="Search Alphabetically",
            bootstyle="info",
            width=30,
            command=create_alphabetical_page
        )
        self.button3.grid(row=1, column=0, padx=(0, 20), pady=(0, 10), ipadx=15, ipady=10)

        # button 4
        self.button4 = ttk.Button(
            self.button_frame,
            text="Search By Ingredient",
            bootstyle="info",
            width=30,
            command=create_ingredient_page
        )
        self.button4.grid(row=1, column=1, padx=20, pady=(0, 10), ipadx=15, ipady=10)
        # -----------------------------------RIGHT IMAGE----------------------------------------------------------------
        self.right_image_raw = Image.open(RIGHT_DRINK)
        self.right_image_resize = self.right_image_raw.resize((130, 200), Image.ANTIALIAS)
        self.right_image = ImageTk.PhotoImage(self.right_image_resize)
        self.right_content = ttk.Label(
            self,
            image=self.right_image
        )
        self.right_content.grid(row=0, column=2, sticky='e')
