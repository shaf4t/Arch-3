from datetime import date

from package import Package
from warehouse_logger import WarehouseLogger


class WarehouseManager:
    def __init__(self):
        self.logger = WarehouseLogger("MANAGER")

    def stores_package_id(self, package_id: str) -> bool:
        return package_id in self.logger.get_all_packages_from_log_file(False)

    def get_all_packages(self) -> tuple[Package, ...]:
        return tuple(self.logger.get_all_packages_from_log_file(False).values())

    def get_total_fee(self) -> float:
        return round(sum(package.get_delivery_fee() for package in self.get_all_packages()), 2)

    def get_total_fee_by_range(self, from_date: date, to_date: date) -> float:
        return round(
            sum(
                package.get_delivery_fee()
                for package in self.get_all_packages()
                if from_date <= package.delivery_date <= to_date
            ),
            2,
        )
