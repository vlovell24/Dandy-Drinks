from Dandy_Drinks.View.home_button_frame import MainButtonGroup
from Dandy_Drinks.Controller.controller import return_random_drink
import ttkbootstrap as ttk
from Dandy_Drinks.Images import LOGO
from Dandy_Drinks.View.title_bar import TitleBar
from Dandy_Drinks.View.main_image import MainImage
from Dandy_Drinks.View.home_text import HomeText
from Dandy_Drinks.View.random_page import RandomPage
from Dandy_Drinks.View.selection_page import SelectionPage

"""
The main application window for the program. First, creates a singleton instance so that only one application can be 
open at one time. An instance variable of self.instance is created with a value of None. This is important later, as 
the value of this variable is what will be referenced when the pages are switched from home page, to random page, etc..
The theme of united is set to the application, and the WM_DELETE_WINDOW command is used to overwrite the 'x' button that
closes the application. This is not currently used, but it could be easily modified to use a confirmation popup/modal.
The title, logo and screen size is set and the window is set to be fixed to a minimum and maximum rather than resizeable
The title bar, gif,home page text and button group classes are packed to the screen. Five methods are used to control
the destruction and creation of the widgets on the screen.
"""


class Application(ttk.Window):
    # -------------------------------SET SINGLETON FOR ONLY ONE INSTANCE OF APP AT ONE TIME-----------------------------
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.__initialized = False
        return cls._instance

    # ------------------------------------CONSTRUCTOR-------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance = None  # used to destroy the pages
        # --------------------------------SET THEME AND DISABLE CLOSE BUTTON--------------------------------------------
        self.style.theme_use('united')
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        # ------------------------------------------TITLE AND LOGO------------------------------------------------------
        self.title("Dandy Drinks")
        self.logo = ttk.PhotoImage(file=LOGO)
        self.iconphoto(False, self.logo)
        # ----------------------------------CENTER SCREEN, SET SIZE, SET RESIZEABLE-------------------------------------
        self.w = 1120
        self.h = 820
        self.ws = self.winfo_screenwidth()
        self.hs = self.winfo_screenheight()
        self.x = (self.ws / 2) - (self.w / 2)
        self.y = (self.hs / 2) - (self.h / 2)
        self.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
        self.minsize(920, 720)
        self.maxsize(1120, 820)
        # -------------------------------------TITLE BAR----------------------------------------------------------------
        self.title_bar = TitleBar(self)
        self.title_bar.pack(fill='x')
        # --------------------------------------GIF---------------------------------------------------------------------
        self.gif = MainImage(self)
        self.gif.pack()
        # --------------------------------------HOME TEXT---------------------------------------------------------------
        self.home_text = HomeText(self)
        self.home_text.pack()
        # --------------------------------------- BOTTOM BUTTONS AND IMAGES---------------------------------------------
        self.bottom_section = MainButtonGroup(self,
                                              self.gif,
                                              self.home_text,
                                              lambda: self.create_page("random"),
                                              lambda: self.create_page("category"),
                                              lambda: self.create_page("alphabetical"),
                                              lambda: self.create_page("ingredient"))
        self.bottom_section.pack(fill='x')

    def destroy_widgets(self):
        """
        Hides the home page widgets
        :return: None; hides the widgets
        """
        self.home_text.pack_forget()
        self.gif.pack_forget()
        self.bottom_section.pack_forget()

    def show_widgets(self):
        """
        Shows the home page widgets
        :return: None; shows home page widgets
        """
        self.gif.pack()
        self.home_text.pack()
        self.bottom_section.pack(fill='x')

    def destroy_page(self, instance):
        """
        Destroys the page instance depending on which class is set to the instance variable at the time. Then calls the
        show_widgets method to recreate the home page.
        :param instance: Class of either RandomPage or SelectionPage
        :return: None; destroys child pages and recreates the home page
        """
        instance.destroy()
        self.show_widgets()

    def create_page(self, page):
        """
        Uses the param page to decide which page type to create to the window. The param 'random' will return the
        RandomPage, while category, alphabetical and ingredient will create the SelectionPage with the page string
        passed in as a parameter. Once the new Class is created, the destroy_widgets method is called to destroy the
        home page classes, and the new instance is packed to the page.
        :param page: string; determines the type of page created.
        :return: None. Creates the new page, and destroys the home page.
        :exception: Exception; very broad exception that covers anything that could go wrong; with most of these being
        related to no internet connection. If the Exception is thrown, then the page simply stays on the home page.
        """
        try:
            if page == "random":
                data = return_random_drink()
                self.instance = RandomPage(self, data, lambda: self.destroy_page(self.instance))
            elif page == "category":
                self.instance = SelectionPage(self, lambda: self.destroy_page(self.instance), "category")
            elif page == "alphabetical":
                self.instance = SelectionPage(self, lambda: self.destroy_page(self.instance), "alphabetical")
            elif page == "ingredient":
                self.instance = SelectionPage(self, lambda: self.destroy_page(self.instance), "ingredient")
            self.destroy_widgets()
            self.instance.pack()
        except Exception:
            return

    def on_close(self):
        """
        Overrides the default close button on the window. Can be used to create a confirmation popup/modal
        :return: None; destroys the application
        """
        self.destroy()
