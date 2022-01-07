from .normal_item import NormalItem


class Conjured(NormalItem):
    def __init__(
        self,
        name,
        sell_in,
        quality,
    ) -> None:
        super(Conjured, self).__init__(
            name,
            sell_in,
            quality,
        )

    def update_quality(self):
        self.pass_day()
        degradation = self.update_degradation()
        if self.quality_can_change():
            self.quality += degradation

    def update_degradation(self):
        return (
            -4
            if self.sell_in < 0
            else -2
        )
