from datetime import date
import os
import unittest

from package import Package
from warehouse_logger import WarehouseLogger


class TestWarehouseLogger(unittest.TestCase):
    def setUp(self):
        if os.path.exists(WarehouseLogger.LOG_FILE):
            os.remove(WarehouseLogger.LOG_FILE)

    def tearDown(self):
        if os.path.exists(WarehouseLogger.LOG_FILE):
            os.remove(WarehouseLogger.LOG_FILE)

    def test_log_and_restore_packages(self):
        logger = WarehouseLogger("Beurs")
        package = Package("P001", 7.3, 16, date(2025, 7, 15))
        logger.log_action("register", package)
        package.update_destination(11.5)
        logger.log_action("update", package)
        logger.log_action("cancel", package)
        self.assertEqual(logger.get_all_packages_from_log_file(), {})

    def test_invalid_action(self):
        with self.assertRaises(ValueError):
            WarehouseLogger("Beurs").log_action(
                "invalid", Package("P001", 1, 1, date.today())
            )


if __name__ == "__main__":
    unittest.main()
