"""
FormattedInstructions is used as a utility/helper/mixin class. It may be used as a Mixin or as an import. Either is
acceptable. This class is used to format the Drink Instruction field for a returned drink. Tkinters Text is used to
create the Instructions for a drink, and the data needs to be formatted correctly. The ingredients are separated by
two before a new line is fed in. The instructions portion of the data is then placed on the text widget after two new
line chars. The Text widget will automatically place a word on a new line if it too long for the box. The None values
for an ingredient measurement are then removed from the formatted document, and it is returned.
"""


class FormattedInstructions:
    @staticmethod
    def formatted_instructions(ingredients, data):
        """
        Formats the instructions text box correctly
        :param ingredients: a list of ingredients
        :param data: list; returned api information. The index of 5 is the instructions.
        :return: string; the instructions for the drink
        """
        formatted_instructions = ""
        for index, ingredient in enumerate(ingredients):
            if index % 2 == 0:
                formatted_instructions += f'{ingredient[0]}: {ingredient[1]}\t\t\t\t'
            else:
                formatted_instructions += f'{ingredient[0]}: {ingredient[1]}\n'
        formatted_instructions += f"\n\n{data[5]}"
        # remove the None values if found in the measurement section. Some ingredients do not have a measurement
        none_removed = formatted_instructions.replace("None", "")
        return none_removed
