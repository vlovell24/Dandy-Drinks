from tkinter import ttk
from PIL import Image, ImageTk
from Dandy_Drinks.Images import BANNER


class TitleBar(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.image_raw = Image.open(BANNER)
        self.image_resize = self.image_raw.resize((820, 100), Image.ANTIALIAS)
        self.resized_image = ImageTk.PhotoImage(self.image_resize)
        self.title_label = ttk.Label(
            self,
            image=self.resized_image
        )
        self.title_label.pack(fill='x')
