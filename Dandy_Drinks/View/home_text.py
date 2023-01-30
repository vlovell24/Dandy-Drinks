from tkinter import BOTH
import ttkbootstrap as ttk

"""
The HomeText class inherits from the tkinter Frame and contains one text Label. This text is what is packed in the 
center of the main home screen.
"""


class HomeText(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.text_label = ttk.Label(
            self,
            text=" It's time for your party, but oh my....what to make?"
                 "Should you\n use brandy? What about vodka? Should you"
                 " provide non-alcoholic?\n What about juices, teas, and/or "
                 "coffee's? Well, here at Dandy\n Drinks, we are all about "
                 "solving your drink dilemmas. Do you need\n specific "
                 "ingredients? Do you need non-alcoholic? Or, are you all\n"
                 "about the random? Make a selection below, choose by "
                 "ingredient,\n glass type, non-alcoholic or just generate a "
                 "random recipe. It's\n all in your hands.",
            font=("Ariel", 16),
            anchor='center',
            bootstyle="info"
        )
        self.text_label.pack(fill=BOTH, pady=20, expand=True)
