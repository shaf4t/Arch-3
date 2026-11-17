from datetime import date
import json
import os
import unittest

from package import Package
from warehouse_logger import WarehouseLogger


class TestWarehouseLogger(unittest.TestCase):
    STATE_FILE = "Beurs_state.json"
    SUMMARY_FILE = "summary_per_date.csv"

    def setUp(self):
        for filename in (self.STATE_FILE, self.SUMMARY_FILE):
            path = os.path.join(os.getcwd(), filename)
            if os.path.exists(path):
                os.remove(path)

    def tearDown(self):
        for filename in (self.STATE_FILE, self.SUMMARY_FILE):
            path = os.path.join(os.getcwd(), filename)
            if os.path.exists(path):
                os.remove(path)

    def test_update_and_restore_state(self):
        logger = WarehouseLogger("Beurs")
        package = Package("P001", 7.3, 16, date(2025, 7, 15))
        logger.update_state({package.id: package})
        with open(self.STATE_FILE, encoding="utf-8") as state_file:
            self.assertEqual(json.load(state_file)[0]["delivery_date"], "2025-07-15")
        restored = logger.get_packages_from_state_file()
        self.assertEqual(restored["P001"].delivery_date, date(2025, 7, 15))


if __name__ == "__main__":
    unittest.main()
