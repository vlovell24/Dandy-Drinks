from tkinter import ttk
from PIL import Image, ImageTk
from Dandy_Drinks.Images import TOP_LEFT, TOP_RIGHT, TITLE_TEXT

"""
TitleBar is a class that inherits from the tkinter Frame. This class creates the image banner on the main page and 
packs it to the screen. The banner image consists of three separate images. The two drinks, and the title text. Each of
these elements are resized and applied to the frame in a tkinter Label. The label is attached to the frame via the grid
method. The background of the image label must be set to the color of the bootstyle 'info' which is #17A2B8 in hex. The
top banner is now dynamic and will resize appropriately.
"""


class TitleBar(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.configure(bootstyle='info')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=1)
        # -------------------------------------TOP LEFT IMAGE-----------------------------------------------------------
        self.left_image_raw = Image.open(TOP_LEFT)
        self.left_resize = self.left_image_raw.resize((40, 80), Image.ANTIALIAS)
        self.left_complete = ImageTk.PhotoImage(self.left_resize)
        self.left_text_label = ttk.Label(
            self,
            image=self.left_complete,
            background='#17A2B8',
            anchor='e'
        )
        self.left_text_label.grid(row=0, column=0, pady=10, padx=10)
        # -------------------------------------CENTER TEXT IMAGE--------------------------------------------------------
        self.center_text_raw = Image.open(TITLE_TEXT)
        self.center_resize = self.center_text_raw.resize((500, 50), Image.ANTIALIAS)
        self.center_complete = ImageTk.PhotoImage(self.center_resize)
        self.center_text_label = ttk.Label(
            self,
            image=self.center_complete,
            background='#17A2B8'
        )
        self.center_text_label.grid(row=0, column=1, pady=10)
        # ---------------------------------------TOP RIGHT IMAGE--------------------------------------------------------
        self.right_image_raw = Image.open(TOP_RIGHT)
        self.right_resize = self.right_image_raw.resize((40, 80), Image.ANTIALIAS)
        self.right_complete = ImageTk.PhotoImage(self.right_resize)
        self.right_image_label = ttk.Label(
            self,
            image=self.right_complete,
            background='#17A2B8',
            anchor='w'
        )
        self.right_image_label.grid(row=0, column=2, pady=10, padx=10)
