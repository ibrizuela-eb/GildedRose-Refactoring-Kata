from .normal_item import NormalItem


class Cheese(NormalItem):
    def __init__(
        self,
        name,
        sell_in,
        quality,
    ) -> None:
        super(Cheese, self).__init__(
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
            2
            if self.sell_in < 0
            else 1
        )
