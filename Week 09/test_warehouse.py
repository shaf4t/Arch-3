from datetime import date
import unittest

from package import Package
from warehouse import Warehouse


class TestWarehouse(unittest.TestCase):
    def setUp(self):
        self.warehouse = Warehouse(2)
        self.package = Package("p01", 5.1, 18.7, date(2025, 4, 18))

    def test_register_package(self):
        self.assertTrue(self.warehouse.register_package(self.package))
        self.assertFalse(self.warehouse.register_package(self.package))

    def test_register_package_capacity(self):
        self.warehouse.register_package(self.package)
        second_package = Package("p02", 2.0, 10.0, date(2025, 5, 1))
        third_package = Package("p03", 2.0, 10.0, date(2025, 5, 1))
        self.warehouse.register_package(second_package)
        self.assertFalse(self.warehouse.register_package(third_package))

    def test_update_destination(self):
        self.warehouse.register_package(self.package)
        self.assertTrue(self.warehouse.update_destination("p01", 25.0))
        self.assertEqual(self.package.travel_distance, 25.0)
        self.assertFalse(self.warehouse.update_destination("missing", 25.0))

    def test_cancel_package(self):
        self.warehouse.register_package(self.package)
        self.assertIs(self.warehouse.cancel_package("p01"), self.package)
        self.assertIsNone(self.warehouse.cancel_package("p01"))

    def test_get_package(self):
        self.warehouse.register_package(self.package)
        self.assertIs(self.warehouse.get_package("p01"), self.package)
        self.assertIsNone(self.warehouse.get_package("missing"))

    def test_get_packages(self):
        self.warehouse.register_package(self.package)
        self.assertEqual(self.warehouse.get_packages(), (self.package,))


if __name__ == "__main__":
    unittest.main()
