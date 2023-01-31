from tkinter import ttk, LEFT, CENTER, TOP
from PIL import Image, ImageTk
from Dandy_Drinks.Images import BANNER, TOP_LEFT, TOP_RIGHT, TITLE_TEXT

"""
TitleBar is a class that inherits from the tkinter Frame. This class creates the image banner on the main page and 
packs it to the screen. The banner image supplied does not need to be presized as this class opens the image and 
resizes it with the PIL library function 'resize'. It then applies antialias to the image (what i call jiggidy lines)
and places the image in a tkinter label. This is then packed to whatever widget it is called from. The image is hard
coded, but an image parameter could be added and any image could be passed in. Furthermore, the resize values could 
also be added to the parameters and the image could be resized at any sized needed. 
"""


# class TitleBar(ttk.Frame):
#     def __init__(self, parent):
#         ttk.Frame.__init__(self, parent)
#         self.image_raw = Image.open(BANNER)
#         self.image_resize = self.image_raw.resize((1020, 100), Image.ANTIALIAS)
#         self.resized_image = ImageTk.PhotoImage(self.image_resize)
#         self.title_label = ttk.Label(
#             self,
#             image=self.resized_image
#         )
#         self.title_label.pack(fill='x')


class TitleBar(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.configure(bootstyle='info')
        # -------------------------------------TOP LEFT IMAGE-----------------------------------------------------------
        self.left_image_raw = Image.open(TOP_LEFT)
        self.left_resize = self.left_image_raw.resize((40, 80), Image.ANTIALIAS)
        self.left_complete = ImageTk.PhotoImage(self.left_resize)
        self.left_text_label = ttk.Label(
            self,
            image=self.left_complete,
            background='#17A2B8'
        )
        self.left_text_label.pack(side=LEFT, pady=10, padx=10)
        # -------------------------------------CENTER TEXT IMAGE--------------------------------------------------------
        self.center_text_raw = Image.open(TITLE_TEXT)
        self.center_resize = self.center_text_raw.resize((500, 50), Image.ANTIALIAS)
        self.center_complete = ImageTk.PhotoImage(self.center_resize)
        self.center_text_label = ttk.Label(
            self,
            image=self.center_complete,
            background='#17A2B8'
        )
        self.center_text_label.pack(side=TOP, pady=10)
