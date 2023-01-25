import io
import urllib.request
import ttkbootstrap as ttk
from Controller.controller import return_drinks_by_category
from PIL import Image, ImageTk
from Controller.controller import return_categories


class CategoryPage(ttk.Frame):
    """Layout for the category page"""

    def __init__(self, parent, category_data):
        ttk.Frame.__init__(self, parent)
        self.category_data = category_data
        # -----------------------------------------FRAME FOR TOP DROPDOWNS----------------------------------------------
        self.dropdown_frame = ttk.Frame(self)
        self.dropdown_frame.grid(row=0, column=0, sticky='nsew')
        self.dropdown_frame.columnconfigure(0, weight=1)
        # -----------------------------------------DROPDOWN ONE/CATEGORIES----------------------------------------------
        self.category_combobox_label = ttk.Label(
            self.dropdown_frame,
            font=("Comic Sans MS", 12),
            text="Select a Drink Category",
            bootstyle="info"
        )
        self.category_combobox_label.grid(row=0, column=0, pady=5)
        self.category_combobox = ttk.Combobox(
            self.dropdown_frame,
            bootstyle='info',
            state='readonly',
            width=50
        )
        self.category_combobox.grid(row=1, column=0)
        self.category_combobox['values'] = self.category_data  # set values to category_data list
        self.category_combobox.current(0)  # default value is set to the first entry
        self.category_combobox.bind('<<ComboboxSelected>>', self.category_change)
        # ---------------------------------------------DROPDOWN TWO/SELECT DRINK----------------------------------------
        self.select_drink_label = ttk.Label(
            self.dropdown_frame,
            font=("Comic Sans MS", 12),
            text="Select a Drink",
            bootstyle='info'
        )
        self.select_drink_label.grid(row=2, column=0, pady=5)
        self.select_drink_combobox = ttk.Combobox(
            self.dropdown_frame,
            bootstyle='info',
            state='readonly',
            width=50
        )
        self.select_drink_combobox.grid(row=3, column=0)
        self.select_drink_combobox['values'] = return_drinks_by_category(self.category_combobox.get())
        self.select_drink_combobox.current(0)

    def category_change(self, event):
        # get drink types data
        drinks = return_drinks_by_category(self.category_combobox.get())
        # set values in select drink combobox
        self.select_drink_combobox['values'] = drinks
        # set current value to the new values
        self.select_drink_combobox.current(0)
        # clear the text highlighting ewwww
        self.category_combobox.selection_clear()
