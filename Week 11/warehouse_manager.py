from datetime import date

from package import Package
from warehouse_logger import WarehouseLogger


class WarehouseManager:
    def __init__(self):
        self.logger = WarehouseLogger("MANAGER")

    def stores_package_id(self, package_id: str) -> bool:
        return package_id in self.logger.get_packages_from_all_state_files()

    def get_all_packages(self) -> tuple[Package, ...]:
        return tuple(self.logger.get_packages_from_all_state_files().values())

    def get_total_fee(self) -> float:
        return round(
            sum(package.get_delivery_fee() for package in self.get_all_packages()), 2
        )

    def get_total_fee_by_range(self, from_date: date, to_date: date) -> float:
        return round(
            sum(
                package.get_delivery_fee()
                for package in self.get_all_packages()
                if from_date <= package.delivery_date <= to_date
            ),
            2,
        )

    def get_all_packages_by_delivery_date(self) -> dict[date, tuple[Package, ...]]:
        packages_by_date: dict[date, list[Package]] = {}
        for package in self.get_all_packages():
            packages_by_date.setdefault(package.delivery_date, []).append(package)
        return {
            delivery_date: tuple(packages)
            for delivery_date, packages in sorted(packages_by_date.items())
        }
