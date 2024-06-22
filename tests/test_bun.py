import pytest
from data import Data
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize('name, price', [(Data.BLACK_BUN, Data.PRICE_BLACK_BUN),
                                             (Data.WHITE_BUN, Data.PRICE_WHITE_BUN),
                                             (Data.SESAME_BUN, Data.PRICE_SESAME_BUN)
                                             ])
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', [(Data.BLACK_BUN, Data.PRICE_BLACK_BUN),
                                             (Data.WHITE_BUN, Data.PRICE_WHITE_BUN),
                                             (Data.SESAME_BUN, Data.PRICE_SESAME_BUN)
                                             ])
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
