from .item import Item
from ..constants import MAX_ITEM_QUALITY


class NormalItem(Item):
    def __init__(
        self,
        name,
        sell_in,
        quality,
    ) -> None:
        super(NormalItem, self).__init__(
            name,
            sell_in,
            quality,
        )

    def pass_day(self):
        self.sell_in -= 1

    def update_quality(self):
        self.pass_day()
        degradation = self.update_degradation()
        if self.quality_can_change():
            self.quality += degradation

    def quality_can_change(self):
        return True if 0 < self.quality < MAX_ITEM_QUALITY else False

    def update_degradation(self):
        return (
            -2
            if self.sell_in < 0
            else -1
        )
