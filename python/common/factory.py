from . import (
    CHEESE_ITEM_NAMES,
    CONJURED_ITEM_NAMES,
    SULFURAS_ITEM_NAMES,
    TICKET_ITEM_NAMES,
)
from python.src.classes.item import Item
from ..src.classes.cheese import Cheese
from ..src.classes.conjured import Conjured
from ..src.classes.normal_item import NormalItem
from ..src.classes.sulfuras import Sulfuras
from ..src.classes.ticket import Ticket


class Factory:
    def __init__(self, items=[]):
        self.items = self.parse_items(items)

    def parse_items(self, items):
        return [
            self.create_new_item(item)
            for item
            in items
        ]

    def get_item_class(self, item_name):
        if item_name in CHEESE_ITEM_NAMES:
            return Cheese
        elif item_name in CONJURED_ITEM_NAMES:
            return Conjured
        elif item_name in SULFURAS_ITEM_NAMES:
            return Sulfuras
        elif item_name in TICKET_ITEM_NAMES:
            return Ticket
        return NormalItem

    def create_new_item(self, item):
        item_class = self.get_item_class(item.name)
        return item_class(
            name=item.name,
            sell_in=item.sell_in,
            quality=item.quality,
        )
