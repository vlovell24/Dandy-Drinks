import ttkbootstrap as ttk
from PIL import Image, ImageTk
from Images import RIGHT_IMAGE
from Images import LEFT_IMAGE


class MainButtonGroup(ttk.Frame):
    """group of four buttons and two images"""

    def __init__(self, parent, gif, text_area, destroy_widgets, create_category_page):
        ttk.Frame.__init__(self, parent)
        self.gif = gif
        self.text_area = text_area
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=1)
        # -----------------------------------LEFT IMAGE-----------------------------------------------------------------
        self.left_image_raw = Image.open(LEFT_IMAGE)
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
        # -------------------------------------BUTTONS------------------------------------------------------------------
        self.button1 = ttk.Button(
            self.button_frame,
            text="Search By Drink Categories",
            bootstyle="primary-outline",
            width=20,
            command=create_category_page
        )
        self.button1.grid(row=0, column=0, padx=(0, 20), pady=(0, 10), ipadx=15, ipady=10)

        # button 2
        self.button2 = ttk.Button(
            self.button_frame,
            text="Select Random",
            bootstyle="primary-outline",
            width=20,
            command=destroy_widgets
        )
        self.button2.grid(row=0, column=1, padx=20, pady=(0, 10), ipadx=15, ipady=10)

        # button 3
        self.button3 = ttk.Button(
            self.button_frame,
            text="Search By First Letter",
            bootstyle="primary-outline",
            width=20
        )
        self.button3.grid(row=1, column=0, padx=(0, 20), pady=(0, 10), ipadx=15, ipady=10)

        # button 4
        self.button4 = ttk.Button(
            self.button_frame,
            text="Search By Ingredient",
            bootstyle="primary-outline",
            width=20
        )
        self.button4.grid(row=1, column=1, padx=20, pady=(0, 10), ipadx=15, ipady=10)
        # -----------------------------------RIGHT IMAGE----------------------------------------------------------------
        self.right_image_raw = Image.open(RIGHT_IMAGE)
        self.right_image_resize = self.right_image_raw.resize((120, 190), Image.ANTIALIAS)
        self.right_image = ImageTk.PhotoImage(self.right_image_resize)
        self.right_content = ttk.Label(
            self,
            image=self.right_image
        )
        self.right_content.grid(row=0, column=2, sticky='e')

    # -------------------------------------------METHODS----------------------------------------------------------------

