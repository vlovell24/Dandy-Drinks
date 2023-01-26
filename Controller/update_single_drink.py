from tkinter import ttk, END
from Controller.formatted_instructions import FormattedInstructions


class UpdateSingleDrink:
    """Utility class to update the values for one single drink"""
    @staticmethod
    def update_single_drink(data, drink_name, category, alcoholic, glass, instructions):
        ingredients = data[6:]
        drink_name['text'] = data[0]
        category['text'] = data[1]
        alcoholic['text'] = data[2]
        glass['text'] = data[3]
        instructions['state'] = 'normal'
        instructions.delete(1.0, END)
        new_instructions = FormattedInstructions.formatted_instructions(ingredients, data)
        instructions.insert(END, new_instructions)
        instructions['state'] = 'disabled'
