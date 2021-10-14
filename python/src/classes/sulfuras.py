from .item import Item


class Sulfuras(Item):
    def __init__(
        self,
        name,
        sell_in,
        quality=80,
    ) -> None:
        super(Sulfuras, self).__init__(
            name,
            sell_in,
            quality=quality,
        )

    def update_quality(self):
        pass
