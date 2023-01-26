import io
import urllib.request
from tkinter import BOTH
from Controller.format_image import FormatImage
import ttkbootstrap as ttk
from Controller.controller import return_drinks_by_category, return_random_drink
from PIL import Image, ImageTk


class CategoryPage(ttk.Frame):
    """Layout for the category page"""

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
        data = self.return_drink_change(drink_name)
        self.modify_drink_info(data)

    def drink_type_change(self, event):
        self.drink_selection_var.set(self.select_drink_combobox.get())
        self.select_drink_combobox.selection_clear()
        drink_name = self.drink_selection_var.get()
        data = self.return_drink_change(drink_name)
        self.modify_drink_info(data)


    def return_drink_change(self, drink_name):
        url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={drink_name}'
        return return_random_drink(url)

    def modify_drink_info(self, data):
        ingredients = data[6:]
        drink_image = FormatImage.format_image(data)
        self.image = drink_image
        self.drink_name['text'] = data[0]
        self.image_label['image'] = drink_image
        self.category_text['text'] = data[1]
        self.alcoholic_text['text'] = data[2]
        self.glass_text['text'] = data[3]
        # assign instructions including the ingredients/measurements
        self.instructions_text['state'] = 'normal' # enable text field
        self.instructions_text.delete(1.0, ttk.END) # delete the contents
        new_instructions = self.formatted_data_for_instructinos_field(ingredients, data)
        self.instructions_text.insert(ttk.END, new_instructions)  # replace the contents
        self.instructions_text['state'] = 'disabled'  # disable the text field again

    def formatted_data_for_instructinos_field(self, ingredient_list, data_list):
        formatted_instructions = ""
        for index, ingredient in enumerate(ingredient_list):
            if index % 2 == 0:
                formatted_instructions += f"{ingredient[0]}: {ingredient[1]}\t\t\t\t"
            else:
                formatted_instructions += f"{ingredient[0]}: {ingredient[1]}\n"

        formatted_instructions += f"\n\n{data_list[5]}"
        # remove the None values if found in the measurement section. Some ingredients do not have a measurement
        none_removed = formatted_instructions.replace("None", "")
        return none_removed
