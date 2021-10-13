import unittest

from ..src.classes.cheese import Cheese


class CheeseTest(unittest.TestCase):

    def test_should_pass_a_day_when_is_called(self):
        cheese = Cheese(
            name='Aged Brie',
            sell_in=10,
            quality=20,
        )
        cheese.pass_day()
        self.assertEqual(9, cheese.sell_in)

    def test_should_degradate_by_1_for_days_before_sell_date(self):
        cheese = Cheese(
            name='Aged Brie',
            sell_in=10,
            quality=20,
        )
        cheese.update_quality()
        self.assertEqual(21, cheese.quality)

    def test_should_increase_degradation_for_days_after_sell_date(self):
        cheese = Cheese(
            name='Aged Brie',
            sell_in=0,
            quality=20,
        )
        cheese.update_quality()
        self.assertEqual(22, cheese.quality)

    def test_degradation_should_maintain_before_sell_date_expire(self):
        cheese = Cheese(
            name='Aged Brie',
            sell_in=1,
            quality=20,
        )
        self.assertEqual(1, cheese.update_degradation())

    def test_degradation_should_modify_after_sell_date_expire(self):
        cheese = Cheese(
            name='Aged Brie',
            sell_in=-1,
            quality=20,
        )
        self.assertEqual(2, cheese.update_degradation())

    def test_should_allow_change_quality(self):
        cheese = Cheese(name='Aged Brie', sell_in=10, quality=1)
        self.assertTrue(cheese.quality_can_change())

    def test_should_not_allow_change_quality(self):
        cheese = Cheese(
            name='Aged Brie',
            sell_in=10,
            quality=50,
        )
        self.assertFalse(cheese.quality_can_change())
