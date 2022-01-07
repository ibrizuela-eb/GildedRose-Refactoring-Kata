import unittest
from . import test_cheese
from . import test_conjured
from . import test_gilded_rose
from . import test_item_factory
from . import test_sulfuras


def create_suite(module):
    suite = unittest.TestSuite()
    suite = unittest.defaultTestLoader.loadTestsFromModule(module)
    return suite


def create_suite_pack():
    suite_list = []
    suite_list.append(create_suite(test_cheese))
    suite_list.append(create_suite(test_conjured))
    suite_list.append(create_suite(test_gilded_rose))
    suite_list.append(create_suite(test_item_factory))
    suite_list.append(create_suite(test_sulfuras))
    return suite_list


if __name__ == '__main__':
    suite_pack = unittest.TestSuite(create_suite_pack())
    runner = unittest.TextTestRunner(descriptions=True, verbosity=3)
    runner.run(suite_pack)
