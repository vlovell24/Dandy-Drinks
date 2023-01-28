from tkinter import BOTH

import ttkbootstrap as ttk
from Controller.controller import return_drinks_by_letter, return_random_drink, return_drinks_by_category, \
    return_categories, return_ingredients, return_drinks_by_ingredient
from Controller.format_image import FormatImage

class SelectionPage(ttk.Frame, FormatImage):
    """Layout for the search alphabetically page"""

    def __init__(self, parent, destroy_page_method, page_type):
        ttk.Frame.__init__(self, parent)
        self.page_type = page_type
        self.category_data = self.get_data_type()  # categories list
        self.dropdown_one_text = self.set_dropdown_one_text()
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
            text=self.dropdown_one_text,
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
        self.select_drink_combobox['values'] = self.drink_default_value()
        self.select_drink_combobox.current(0)  # set default to zero value

        self.select_drink_combobox.bind('<<ComboboxSelected>>', self.drink_change)
        self.bind('<Visibility>', self.drink_change)
        # ------------------------------------------------------DRINK NAME----------------------------------------------
        self.drink_name = ttk.Label(
            self.dropdown_frame,
            bootstyle='info',
            font=("Comic Sans MS", 20, "bold")
        )
        self.drink_name.grid(row=4, column=0, pady=20)
        # ----------------------------------------------------BOTTOM FRAME----------------------------------------------
        self.bottom_frame = ttk.Frame(self)
        self.bottom_frame.grid(row=1, column=0, sticky='nsew')
        # ----------------------------------------------------LEFT DRINK IMAGE FRAME------------------------------------
        self.drink_image_frame = ttk.Frame(self.bottom_frame)
        self.drink_image_frame.pack(side='left', expand=True, fill=BOTH)
        # -------------------------------------------------------DRINK IMAGE--------------------------------------------
        self.image = ''
        self.image_label = ttk.Label(
            self.bottom_frame,
            bootstyle='inverse-secondary',
            anchor='center',
            image=self.image
        )
        self.image_label.pack(ipadx=20, ipady=10, side='left')
        # ----------------------------------------------------RIGHT INFORMATION FRAME-----------------------------------
        self.info_frame = ttk.Frame(self.bottom_frame)
        self.info_frame.pack(side='left', expand=True, fill=BOTH)
        # ----------------------------------------------------CATEGORY LABELFRAME---------------------------------------
        self.category_label = ttk.LabelFrame(
            self.info_frame,
            text="Drink Category",
            bootstyle='info'
        )
        self.category_label.grid(row=0, column=0, pady=(10, 10), padx=20, sticky='ew')
        # ----------------------------------------------------CATEGORY TEXT---------------------------------------------
        self.category_text = ttk.Label(
            self.category_label,
            text="Testing here",
            font=("Comic Sans MS", 10, 'bold'),
            width=50
        )
        self.category_text.pack(fill='x', side='top', expand=True)
        # ----------------------------------------------------ALCOHOLIC LABELFRAME--------------------------------------
        self.alcoholic = ttk.LabelFrame(
            self.info_frame,
            text="Alcoholic or Non",
            bootstyle='info'
        )
        self.alcoholic.grid(row=1, column=0, pady=(0, 10), padx=(20, 20), sticky='ew')
        # -------------------------------------------------------ALCOHOLIC TEXT-----------------------------------------
        self.alcoholic_text = ttk.Label(
            self.alcoholic,
            text="Testing alcohol",
            font=("Comic Sans MS", 10, 'bold'),
            width=50
        )
        self.alcoholic_text.pack(fill='x', side='top', expand=True)
        # --------------------------------------------------GLASS TYPE LABELFRAME---------------------------------------
        self.glass_frame = ttk.LabelFrame(
            self.info_frame,
            text="Glass Type",
            bootstyle='info'
        )
        self.glass_frame.grid(row=2, column=0, pady=(0, 10), padx=20, sticky='ew')
        # ----------------------------------------------------GLASS TEXT------------------------------------------------
        self.glass_text = ttk.Label(
            self.glass_frame,
            text="Testing glass",
            font=("Comic Sans MS", 10, 'bold'),
            width=50
        )
        self.glass_text.pack(fill='x', side='top', expand=True)
        # ------------------------------------------------INSTRUCTIONS LABELFRAME---------------------------------------
        self.instructions_frame = ttk.LabelFrame(
            self.info_frame,
            text="Instructions",
            bootstyle='info'
        )
        self.instructions_frame.grid(row=3, column=0, pady=(0, 10), padx=20, sticky='ew')
        # ----------------------------------------------INSTRUCTIONS TEXT-----------------------------------------------
        self.instructions_text = ttk.Text(
            self.instructions_frame,
            wrap="word",
            width=50,
            height=12
        )
        self.instructions_text.pack(fill=BOTH, side='top', expand=True)
        self.instructions_text['state'] = 'disabled'

    def set_dropdown_one_text(self):
        text = ""
        if self.page_type == "alphabetical":
            text = "Select a Letter"
        elif self.page_type == "category":
            text = "Select a Drink Category"
        elif self.page_type == "ingredient":
            text = "Select a Ingredient"
        return text

    def category_change(self, event):
        drinks = []
        if self.page_type == "alphabetical":
            drinks = return_drinks_by_letter(self.category_combobox.get())
        elif self.page_type == "category":
            drinks = return_drinks_by_category(self.category_combobox.get())
        elif self.page_type == "ingredient":
            drinks = return_drinks_by_ingredient(self.category_combobox.get())
        self.select_drink_combobox['values'] = drinks
        self.select_drink_combobox.current(0)
        self.category_combobox.selection_clear()
        self.drink_change(None)  # to update the drink stringvar

    def get_data_type(self):
        return_data = []
        if self.page_type == "category":
            return_data = return_categories()
        elif self.page_type == "alphabetical":
            return_data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        elif self.page_type == "ingredient":
            return_data = return_ingredients()
        return return_data

    def drink_default_value(self):
        """
        Gets the values to fill the select_drink combobox by calling the api and passing in the value of the
        category_combobox. These values are returned as the dropdown values of the select_drink combobox
        :return: List; values for the select_drink combobox
        """
        if self.page_type == "category":
            return return_drinks_by_category(self.category_combobox.get())
        elif self.page_type == "alphabetical":
            return return_drinks_by_letter(self.category_combobox.get())
        elif self.page_type == "ingredient":
            return return_drinks_by_ingredient(self.category_combobox.get())

    def drink_change(self, event):
        # set the drink stringvar value
        self.drink_selection_var.set(self.select_drink_combobox.get())
        self.select_drink_combobox.selection_clear()  # clear the highlighting
        drink_name = self.drink_selection_var.get()
        url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={drink_name}'
        return return_random_drink(new_url=url)


    # def modify_drink_values_on_page(self, data):
    #     drink_image = self.format_image(data)
