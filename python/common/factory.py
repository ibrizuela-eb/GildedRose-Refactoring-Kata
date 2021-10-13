from . import ITEM_CLASES


class Factory:
    def __init__(self, items=[]):
        self.items = self.parse_items(items)

    def parse_items(self, items):
        return [
            self.create_new_item(item)
            for item
            in items
        ]

    def create_new_item(self, item):
        return ITEM_CLASES[item.name](
            name=item.name,
            sell_in=item.sell_in,
            quality=item.quality,
        )
