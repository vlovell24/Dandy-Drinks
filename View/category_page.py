
import ttkbootstrap as ttk
from Controller.controller import return_drinks_by_category, return_random_drink
from PIL import Image, ImageTk


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
        self.category_combobox.bind('<<ComboboxSelected>>', self.category_change)  # binding box one
        # ---------------------------------------------DROPDOWN TWO/SELECT DRINK----------------------------------------
        self.drink_selection_var = ttk.StringVar()  # set to the value of the select drink combobox whenever changed
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
        self.select_drink_combobox.bind('<<ComboboxSelected>>', self.drink_type_change)  # binding box two
        # create a default drink when page loads, defaults to whatever is in the combobox
        self.bind("<Visibility>", self.drink_type_change)

    def category_change(self, event):
        # get drink types data
        drinks = return_drinks_by_category(self.category_combobox.get())
        # set values in select drink combobox
        self.select_drink_combobox['values'] = drinks
        # set current value to the new values
        self.select_drink_combobox.current(0)
        # clear the text highlighting ewwww
        self.category_combobox.selection_clear()
        self.drink_selection_var.set(self.select_drink_combobox.get())
        drink_name = self.drink_selection_var.get()
        self.return_drink_change(drink_name)

    def drink_type_change(self, event):
        self.drink_selection_var.set(self.select_drink_combobox.get())
        self.select_drink_combobox.selection_clear()
        drink_name = self.drink_selection_var.get()
        self.return_drink_change(drink_name)

    def return_drink_change(self, drink_name):
        url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={drink_name}'
        print(return_random_drink(url))
