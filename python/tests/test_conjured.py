from parameterized import parameterized
import unittest

from ..src.conjured import Conjured


class ConjuredTets(unittest.TestCase):

    def test_should_pass_a_day_when_is_called(self):
        vest = Conjured(
            name='+5 Dexterity Vest',
            sell_in=10,
            quality=20,
        )
        vest.pass_day()
        self.assertEqual(9, vest.sell_in)

    def test_should_degradate_by_2_for_days_before_sell_date(self):
        vest = Conjured(
            name='+5 Dexterity Vest',
            sell_in=10,
            quality=20,
        )
        vest.update_quality()
        self.assertEqual(18, vest.quality)

    def test_should_increase_degradation_for_days_after_sell_date(self):
        vest = Conjured(
            name='+5 Dexterity Vest',
            sell_in=0,
            quality=20,
        )
        vest.update_quality()
        self.assertEqual(16, vest.quality)

    def test_degradation_should_maintain_before_sell_date_expire(self):
        vest = Conjured(
            name='+5 Dexterity Vest',
            sell_in=1,
            quality=20,
        )
        self.assertEqual(-2, vest.update_degradation())

    def test_degradation_should_modify_after_sell_date_expire(self):
        vest = Conjured(
            name='+5 Dexterity Vest',
            sell_in=-1,
            quality=20,
        )
        self.assertEqual(-4, vest.update_degradation())

    @parameterized.expand([
        (Conjured(name='+5 Dexterity Vest', sell_in=10, quality=1),),
        (Conjured(name='+5 Dexterity Vest', sell_in=10, quality=20),),
    ])
    def test_should_allow_change_quality(self, vest):
        self.assertTrue(vest.quality_can_change())

    def test_should_not_allow_change_quality(self):
        vest = Conjured(
            name='+5 Dexterity Vest',
            sell_in=10,
            quality=0,
        )
        self.assertFalse(vest.quality_can_change())
