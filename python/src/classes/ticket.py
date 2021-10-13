from .item import Item


class Ticket(Item):
    def __init__(
        self,
        name,
        sell_in,
        quality,
    ) -> None:
        super(Ticket, self).__init__(
            name,
            sell_in,
            quality,
        )

    def pass_day(self):
        self.sell_in -= 1

    def update_quality(self):
        self.pass_day()
        degradation = self.update_degradation()
        if self.sell_in >= 0:
            if self.quality_can_change():
                self.quality += degradation
        else:
            self.quality = 0

    def quality_can_change(self):
        return True if self.quality < 50 else False

    def update_degradation(self):
        if self.sell_in > 10:
            return 1
        elif 5 < self.sell_in < 10:
            return 2
        elif 0 <= self.sell_in < 5:
            return 3
        return 0
