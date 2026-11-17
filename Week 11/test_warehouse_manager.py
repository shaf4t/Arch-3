from datetime import date
import os
import unittest

from package import Package
from warehouse import Warehouse
from warehouse_manager import WarehouseManager


class TestWarehouseManager(unittest.TestCase):
    STATE_FILE = "Beurs_state.json"

    def setUp(self):
        path = os.path.join(os.getcwd(), self.STATE_FILE)
        if os.path.exists(path):
            os.remove(path)

    def tearDown(self):
        path = os.path.join(os.getcwd(), self.STATE_FILE)
        if os.path.exists(path):
            os.remove(path)

    def test_packages_are_grouped_by_delivery_date(self):
        warehouse = Warehouse("Beurs")
        warehouse.register_package(Package("P001", 1, 10, date(2025, 7, 15)))
        warehouse.register_package(Package("P002", 2, 10, date(2025, 7, 15)))
        grouped = WarehouseManager().get_all_packages_by_delivery_date()
        self.assertEqual(len(grouped[date(2025, 7, 15)]), 2)


if __name__ == "__main__":
    unittest.main()
