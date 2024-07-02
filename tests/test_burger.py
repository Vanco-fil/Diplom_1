from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from data import Data


class TestBurger:

    def test_set_buns(self):
        mock = Mock()
        burger = Burger()
        mock.get_name.return_value = Data.BLACK_BUN
        mock.get_price.return_value = Data.PRICE_BLACK_BUN
        burger.set_buns(mock)
        assert burger.bun.get_name() == Data.BLACK_BUN
        assert burger.bun.get_price() == Data.PRICE_BLACK_BUN

    def test_add_ingredient(self):
        mock = Mock()
        burger = Burger()
        mock.get_price.return_value = Data.PRICE_SPICY_SAUCE
        mock.get_name.return_value = Data.SPICY_SAUCE
        mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
        burger.add_ingredient(mock)
        assert burger.ingredients == [mock]

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SPICY_SAUCE, Data.PRICE_SPICY_SAUCE)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()
        ingredient_0 = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SPICY_SAUCE, Data.PRICE_SPICY_SAUCE)
        ingredient_1 = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SWEET_SAUCE, Data.PRICE_SWEET_SAUCE)
        burger.add_ingredient(ingredient_0)
        burger.add_ingredient(ingredient_1)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1].name == Data.SPICY_SAUCE

    def test_get_price(self):
        burger = Burger()
        bun = Bun(Data.BLACK_BUN, Data.PRICE_BLACK_BUN)
        burger.set_buns(bun)
        sauce_1 = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SPICY_SAUCE, Data.PRICE_SPICY_SAUCE)
        burger.add_ingredient(sauce_1)
        assert burger.get_price() == 19.3

    def test_get_receipt(self):
        mock = Mock()
        burger = Burger()
        mock.get_name.return_value = Data.BLACK_BUN
        mock.get_price.return_value = Data.PRICE_BLACK_BUN
        burger.set_buns(mock)
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SWEET_SAUCE, Data.PRICE_SWEET_SAUCE)
        burger.add_ingredient(sauce)
        assert burger.get_receipt() == Data.RECEIPT
