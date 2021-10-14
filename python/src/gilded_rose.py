# -*- coding: utf-8 -*
from ..common.factory import Factory


class GildedRose(object):

    def __init__(self, items):
        factory = Factory()
        self.items = factory.parse_items(items)

    def update_quality(self):
        for item in self.items:
            item.update_quality()
