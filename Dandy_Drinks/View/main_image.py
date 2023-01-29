from PIL import Image, ImageTk
import ttkbootstrap as ttk
from Dandy_Drinks.Images import MAIN


class MainImage(ttk.Frame):
    """Main image for the home page"""

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
