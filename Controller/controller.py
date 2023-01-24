import json
from pathlib import Path
import requests


def return_random_drink():
    """
    Opens the api and gets a random drink. Once the data is recieved, it must be parsed. It is loaded into a list for
    return. The ingredients and measurements are seperate values and must be forced together and then appended to the
    return list.
    :return: List; return_array
    """
    url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'  # search by random
    return_array = []
    ingredient_array = []
    try:
        data = requests.get(url)
        drinks = json.loads(data.text)
        #print(drinks)
        for array in (drinks["drinks"]):
            return_array.extend([
                array['strDrink'],
                array['strCategory'],
                array['strAlcoholic'],
                array['strGlass'],
                array['strDrinkThumb'],
                array['strInstructions']
            ])
        for array in (drinks["drinks"]):  # map together the ingredients and measurement fields
            ingredient_array.extend([
                (array['strIngredient1'], array['strMeasure1']),
                (array['strIngredient2'], array['strMeasure2']),
                (array['strIngredient3'], array['strMeasure3']),
                (array['strIngredient4'], array['strMeasure4']),
                (array['strIngredient5'], array['strMeasure5']),
                (array['strIngredient6'], array['strMeasure6']),
                (array['strIngredient7'], array['strMeasure7']),
                (array['strIngredient8'], array['strMeasure8']),
                (array['strIngredient9'], array['strMeasure9']),
                (array['strIngredient10'], array['strMeasure10']),
                (array['strIngredient11'], array['strMeasure11']),
                (array['strIngredient12'], array['strMeasure12']),
                (array['strIngredient13'], array['strMeasure13']),
                (array['strIngredient14'], array['strMeasure14']),
                (array['strIngredient15'], array['strMeasure15'])
            ])
        # in the api, a default value of 15 ingredients and 15 measurements are provided, however not all of these are
        # used. Unused fields are marked as None, therefore after we map the ingredient/measurement entries, we will
        # want to remove the None ingredient values only. Some ingredients may have None measurement values, think lime,
        # ice cube, etc. We will filter out None measurement values later.
        for item in ingredient_array:
            if item[0] is not None:
                return_array.append(item)
    except BaseException:  # if we have no connection, return none
        return None

    return return_array


