import ttkbootstrap as ttk
from Controller.controller import return_drinks_by_letter, return_random_drink


class AlphabeticalPage(ttk.Frame):
    """Layout for the search alphabetically page"""

    def __init__(self, parent, category_data, destroy_page_method):
        ttk.Frame.__init__(self, parent)
        self.category_data = category_data  # categories list
        # -----------------------------------------FRAME FOR TOP DROPDOWNS----------------------------------------------
        self.dropdown_frame = ttk.Frame(self)
        self.dropdown_frame.grid(row=0, column=0, sticky='nsew')
        self.dropdown_frame.columnconfigure(0, weight=1)
        # --------------------------------------------HOME BUTTON-------------------------------------------------------
        self.home_button = ttk.Button(
            self.dropdown_frame,
            bootstyle='dark',
            text="Home",
            command=destroy_page_method
        )
        self.home_button.grid(row=0, column=0, sticky='e')
        # -----------------------------------------DROPDOWN ONE/CATEGORIES----------------------------------------------
        self.category_combobox_label = ttk.Label(
            self.dropdown_frame,
            font=("Comic Sans MS", 12),
            text="Select a letter",
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
        # ------------------------------------------DRINKS COMBOBOX-----------------------------------------------------
        self.drink_selection_var = ttk.StringVar()  # set to the value of the select drink combobox whenever changes
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
        self.select_drink_combobox['values'] = return_drinks_by_letter(self.category_combobox.get())
        self.select_drink_combobox.current(0)  # set default to zero value
        self.select_drink_combobox.bind('<<ComboboxSelected>>', self.drink_type_change)
        self.bind('<Visibility>', self.drink_type_change)

    def drink_type_change(self, event):
        self.drink_selection_var.set(self.select_drink_combobox.get())
        self.select_drink_combobox.selection_clear()
        drink_name = self.drink_selection_var.get()
        data = self.return_drink_change(drink_name)

    @staticmethod
    def return_drink_change(drink_name):
        url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={drink_name}'
        return return_random_drink(new_url=url)

    def category_change(self, event):
        drinks = return_drinks_by_letter(self.category_combobox.get())
        self.select_drink_combobox['values'] = drinks
        self.select_drink_combobox.current(0)
        self.category_combobox.selection_clear()
        self.drink_type_change(None)
