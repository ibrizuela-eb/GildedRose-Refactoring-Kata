from .normal_item import NormalItem


class Ticket(NormalItem):
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

    def update_quality(self):
        self.pass_day()
        degradation = self.update_degradation()
        if self.sell_in >= 0:
            if self.quality_can_change():
                self.quality += degradation
        else:
            self.quality = 0

    def update_degradation(self):
        if self.sell_in > 10:
            return 1
        elif 5 < self.sell_in <= 10:
            return 2
        elif 0 <= self.sell_in <= 5:
            return 3
        return 0
