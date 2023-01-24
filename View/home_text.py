from tkinter import BOTH
import ttkbootstrap as ttk


class HomeText(ttk.Frame):
    """A group of text centered inside a frame"""

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
            font=("Comic Sans MS", 16, "bold"),
            anchor='center'
        )
        self.text_label.pack(fill=BOTH, pady=20, expand=True)
