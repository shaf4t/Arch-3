from datetime import date
import os
import unittest

from package import Package
from warehouse import Warehouse
from warehouse_logger import WarehouseLogger
from warehouse_manager import WarehouseManager


class TestWarehouseManager(unittest.TestCase):
    def setUp(self):
        if os.path.exists(WarehouseLogger.LOG_FILE):
            os.remove(WarehouseLogger.LOG_FILE)

    def tearDown(self):
        if os.path.exists(WarehouseLogger.LOG_FILE):
            os.remove(WarehouseLogger.LOG_FILE)

    def test_totals_and_package_lookup(self):
        warehouse = Warehouse("Beurs")
        warehouse.register_package(Package("P001", 1, 10, date(2025, 7, 15)))
        manager = WarehouseManager()
        self.assertTrue(manager.stores_package_id("P001"))
        self.assertEqual(len(manager.get_all_packages()), 1)
        self.assertEqual(manager.get_total_fee_by_range(date(2025, 7, 15), date(2025, 7, 15)), 1.18)


if __name__ == "__main__":
    unittest.main()
