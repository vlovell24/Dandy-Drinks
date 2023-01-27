import ttkbootstrap as ttk


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
