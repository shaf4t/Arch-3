from datetime import date
import unittest

from package import Package


class TestPackage(unittest.TestCase):
    def setUp(self):
        self.package = Package("P001", 5.1, 18.7, date(2025, 4, 18))

    def test_get_delivery_fee(self):
        self.assertEqual(self.package.get_delivery_fee(), 2.03)

    def test_get_details(self):
        self.assertEqual(
            self.package.get_details(),
            "Package(id=P001, weight=5.1, travel_distance=18.7, "
            "delivery_date=2025-04-18)",
        )

    def test_update_destination(self):
        self.package.update_destination(25.0)
        self.assertEqual(self.package.travel_distance, 25.0)


if __name__ == "__main__":
    unittest.main()
