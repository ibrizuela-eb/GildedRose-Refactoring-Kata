# -*- coding: utf-8 -*-
from parameterized import parameterized
import unittest

from ..src.gilded_rose import GildedRose
from ..src.classes.item import Item


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", gilded_rose.items[0].name)

    # TODO
    # This item class should be a normal item
    def test_should_degradate_item_quality_by_2_when_date_has_expired(self):
        items = [Item(name="+5 Dexterity Vest", sell_in=0, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, gilded_rose.items[0].quality)

    def test_quality_could_never_be_negative(self):
        items = [Item(name="+5 Dexterity Vest", sell_in=0, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, gilded_rose.items[0].quality)

    def test_should_upgrade_aged_brie_quality_by_1_each_day_passed(self):
        items = [Item(name="Aged Brie", sell_in=5, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, gilded_rose.items[0].quality)

    def test_should_upgrade_aged_brie_quality_by_2_when_date_has_expired(self):
        items = [Item(name="Aged Brie", sell_in=0, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, gilded_rose.items[0].quality)

    @parameterized.expand([
        (Item(name="Aged Brie", sell_in=1, quality=50),),
        (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=50),),
    ])
    def test_quality_should_never_be_more_than_50(self, item):
        items = [item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, gilded_rose.items[0].quality)

    @parameterized.expand([
        (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=30), 32),
        (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=7, quality=30), 32),
        (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=12, quality=30), 31),
    ])
    def test_should_increase_quality_by_2_if_6_or_10_days_are_missing(self, item, expected):
        items = [item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(expected, gilded_rose.items[0].quality)

    @parameterized.expand([
        (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=30), 33),
        (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=30), 33),
    ])
    def test_should_increase_quality_by_3_if_1_or_5_days_are_missing(self, item, expected):
        items = [item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(expected, gilded_rose.items[0].quality)

    def test_should_drop_quality_of_a_ticket_to_minimum_when_date_expire(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, gilded_rose.items[0].quality)

    """New specifications
    """
    def test_should_degradate_conjured_by_2_when_date_is_before_expire(self):
        items = [Item(name="Conjured Mana Cake", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, gilded_rose.items[0].quality)

    def test_should_not_modify_quality_of_sulfura_item_when_a_day_has_passed(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, gilded_rose.items[0].quality)

    def test_should_not_modify_sell_in_of_sulfura_item_when_a_day_has_passed(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=1, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, gilded_rose.items[0].sell_in)


if __name__ == '__main__':
    unittest.main()
