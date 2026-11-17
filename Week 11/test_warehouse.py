from datetime import date
import os
import unittest

from package import Package
from warehouse import Warehouse


class TestWarehouse(unittest.TestCase):
    STATE_FILE = "Beurs_state.json"

    def setUp(self):
        path = os.path.join(os.getcwd(), self.STATE_FILE)
        if os.path.exists(path):
            os.remove(path)

    def tearDown(self):
        path = os.path.join(os.getcwd(), self.STATE_FILE)
        if os.path.exists(path):
            os.remove(path)

    def test_register_update_cancel_and_restore(self):
        warehouse = Warehouse("Beurs", capacity=2)
        package = Package("P001", 5.1, 18.7, date(2025, 4, 18))
        self.assertTrue(warehouse.register_package(package))
        self.assertTrue(warehouse.update_destination("P001", 25.0))
        restored = Warehouse("Beurs", capacity=2)
        self.assertEqual(restored.get_package("P001").travel_distance, 25.0)
        self.assertIsNotNone(restored.cancel_package("P001"))
        self.assertEqual(restored.get_packages(), ())


if __name__ == "__main__":
    unittest.main()
