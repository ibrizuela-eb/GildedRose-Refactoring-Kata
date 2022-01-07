import unittest
from parameterized import parameterized

from ..common.factory import Factory
from ..src.classes.cheese import Cheese
from ..src.classes.conjured import Conjured
from ..src.classes.item import Item
from ..src.classes.normal_item import NormalItem
from ..src.classes.sulfuras import Sulfuras
from ..src.classes.ticket import Ticket


class ItemFactoryTests(unittest.TestCase):
    @parameterized.expand([
        (Item(name="Aged Brie", sell_in=2, quality=0), Cheese),
        (Item(name="+5 Dexterity Vest", sell_in=10, quality=20), Conjured),
        (Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80), Sulfuras),
        (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20), Ticket),
    ])
    def test_should_create_correct_item(
        self,
        item,
        expected_class,
    ):
        factory = Factory()
        new_item = factory.create_new_item(item)
        self.assertIsInstance(new_item, expected_class)

    def test_should_parse_item_to_its_special_class(self):
        items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
        ]
        factory = Factory()
        new_items = factory.parse_items(items)
        item_classes = list(map(lambda x: type(x), new_items))
        item_classes_expected = [
            Conjured,
            Cheese,
            NormalItem,
            Sulfuras,
            Sulfuras,
            Ticket,
            Ticket,
            Ticket,
            Conjured,
        ]
        self.assertEqual(item_classes, item_classes_expected)
