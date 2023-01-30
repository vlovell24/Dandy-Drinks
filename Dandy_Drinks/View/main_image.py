from PIL import Image, ImageTk
import ttkbootstrap as ttk
from Dandy_Drinks.Images import MAIN

"""
The MainImage class inherits from the tkinter Frame widget. This class creates and packs an image to whatever it is
attached too. The image file is hard coded for the purposes of this application, however it could be changed to a 
parameter value, and then any image could be packed to the frame.
"""

class MainImage(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.image_raw = Image.open(MAIN)
        self.image_resize = self.image_raw.resize((400, 150), Image.ANTIALIAS)
        self.resized_image = ImageTk.PhotoImage(self.image_resize)
        self.image_label = ttk.Label(
            self,
            image=self.resized_image
        )
        self.image_label.pack(fill='x')
