from parameterized import parameterized
import unittest

from ..src.sulfuras import Sulfuras


class SulfurasTets(unittest.TestCase):
    def test_sulfuras_never_change_its_quality(self):
        sulfuras = Sulfuras(
            name='Sulfuras, Hand of Ragnaros',
            sell_in=10,
            quality=80,
        )
        sulfuras.update_quality()
        self.assertEqual(80, sulfuras.quality)

    def test_sulfuras_never_change_its_sell_in(self):
        sulfuras = Sulfuras(
            name='Sulfuras, Hand of Ragnaros',
            sell_in=10,
            quality=80,
        )
        sulfuras.update_quality()
        self.assertEqual(10, sulfuras.sell_in)
