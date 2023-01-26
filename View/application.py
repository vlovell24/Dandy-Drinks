from View.home_button_frame import MainButtonGroup
from Controller.controller import return_random_drink, return_categories
import ttkbootstrap as ttk
from Images import LOGO
from View.title_bar import TitleBar
from View.main_image import MainImage
from View.home_text import HomeText
from View.random_page import RandomPage
from View.category_page import CategoryPage


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
        self.randomInstance = None  # used to destroy the Random Page
        self.categoryInstance = None  # used to destroy the Category Page
        # --------------------------------SET THEME AND DISABLE CLOSE BUTTON--------------------------------------------
        self.style.theme_use('united')
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        # ------------------------------------------TITLE AND LOGO------------------------------------------------------
        self.title("Dandy Drinks")
        self.logo = ttk.PhotoImage(file=LOGO)
        self.iconphoto(False, self.logo)
        # ----------------------------------CENTER SCREEN, SET SIZE, SET RESIZEABLE-------------------------------------
        self.w = 825
        self.h = 720
        self.ws = self.winfo_screenwidth()
        self.hs = self.winfo_screenheight()
        self.x = (self.ws / 2) - (self.w / 2)
        self.y = (self.hs / 2) - (self.h / 2)
        self.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
        self.resizable(False, False)
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
        self.bottom_section = MainButtonGroup(self, self.gif, self.home_text, lambda: self.create_random_page(), lambda: self.create_category_page())
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

    def create_random_page(self):
        # get the random drink data that we want to append to the application window
        url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'
        random_data = return_random_drink(url)
        if random_data:  # if we can connect to the interwebz
            self.destroy_widgets()
            # create random page
            self.create_random_widgets(random_data)
        else:
            return

    def destroy_random_page(self):
        """
        Destroys the random page from the window, and repacks the home pages gif, text and bottom section
        :return: None; destroys random page and shows home page
        """
        self.randomInstance.destroy()
        self.show_widgets()

    def destroy_category_page(self):
        """
        Destroys the category page from the window, and repacks the home page
        :return: None; destroys category page and shows home page
        """
        self.categoryInstance.destroy()
        self.show_widgets()

    def create_random_widgets(self, data):
        self.randomInstance = RandomPage(self, data, lambda: self.destroy_random_page())
        self.randomInstance.pack()

    def create_category_page(self):
        # get categories
        category_data = return_categories()
        # hide home page widgets
        self.destroy_widgets()
        # show category page
        self.categoryInstance = CategoryPage(self, category_data, lambda: self.destroy_category_page())
        self.categoryInstance.pack()

    def on_close(self):
        """Use to create custom close later"""
        self.destroy()
