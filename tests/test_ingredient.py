from data import Data
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, Data.COWBERRY_CREAM, Data.PRICE_COWBERRY_CREAM)
        assert ingredient.get_price() == Data.PRICE_COWBERRY_CREAM

    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SWEET_SAUCE, Data.PRICE_SWEET_SAUCE)
        assert ingredient.get_name() == Data.SWEET_SAUCE

    def test_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SPICY_SAUCE, Data.PRICE_SPICY_SAUCE)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
