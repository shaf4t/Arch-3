from datetime import date
import os
import unittest

from package import Package
from warehouse import Warehouse
from warehouse_logger import WarehouseLogger


class TestWarehouse(unittest.TestCase):
    def setUp(self):
        if os.path.exists(WarehouseLogger.LOG_FILE):
            os.remove(WarehouseLogger.LOG_FILE)
        self.warehouse = Warehouse("Beurs", capacity=2)
        self.package = Package("P001", 5.1, 18.7, date(2025, 4, 18))

    def tearDown(self):
        if os.path.exists(WarehouseLogger.LOG_FILE):
            os.remove(WarehouseLogger.LOG_FILE)

    def test_register_package_and_restore_state(self):
        self.assertTrue(self.warehouse.register_package(self.package))
        restored = Warehouse("Beurs", capacity=2)
        self.assertIsNotNone(restored.get_package("P001"))

    def test_duplicate_and_capacity(self):
        self.assertTrue(self.warehouse.register_package(self.package))
        self.assertFalse(self.warehouse.register_package(self.package))
        second = Package("P002", 1, 1, date(2025, 5, 1))
        third = Package("P003", 1, 1, date(2025, 5, 1))
        self.assertTrue(self.warehouse.register_package(second))
        self.assertFalse(self.warehouse.register_package(third))

    def test_update_destination(self):
        self.warehouse.register_package(self.package)
        self.assertTrue(self.warehouse.update_destination("P001", 25.0))
        self.assertEqual(self.package.travel_distance, 25.0)
        self.assertFalse(self.warehouse.update_destination("missing", 25.0))

    def test_cancel_and_get_packages(self):
        self.warehouse.register_package(self.package)
        self.assertIs(self.warehouse.get_package("P001"), self.package)
        self.assertIs(self.warehouse.cancel_package("P001"), self.package)
        self.assertEqual(self.warehouse.get_packages(), ())
        self.assertIsNone(self.warehouse.cancel_package("P001"))


if __name__ == "__main__":
    unittest.main()
