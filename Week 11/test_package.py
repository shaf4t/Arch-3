from datetime import date
import unittest

from package import Package


class TestPackage(unittest.TestCase):
    def test_convert_to_dict(self):
        package = Package("P001", 5.3, 17.4, date(2025, 5, 4))
        self.assertEqual(
            package.convert_to_dict(),
            {
                "id": "P001",
                "weight": 5.3,
                "travel_distance": 17.4,
                "delivery_date": "2025-05-04",
            },
        )


if __name__ == "__main__":
    unittest.main()
