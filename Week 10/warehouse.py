from package import Package
from warehouse_logger import WarehouseLogger


class Warehouse:
    def __init__(self, id: str, capacity: int = 10):
        self.id = id
        self.capacity = capacity
        self.packages: dict[str, Package] = {}
        self.logger = WarehouseLogger(id)
        self.restore_state()

    def restore_state(self) -> None:
        self.packages = self.logger.get_all_packages_from_log_file()

    def register_package(self, package: Package) -> bool:
        if len(self.packages) >= self.capacity or package.id in self.packages:
            return False

        self.packages[package.id] = package
        self.logger.log_action("register", package)
        return True

    def update_destination(self, package_id: str, new_distance: float) -> bool:
        package = self.packages.get(package_id)
        if package is None:
            return False

        package.update_destination(new_distance)
        self.logger.log_action("update", package)
        return True

    def cancel_package(self, package_id: str) -> Package | None:
        package = self.packages.pop(package_id, None)
        if package is not None:
            self.logger.log_action("cancel", package)
        return package

    def get_package(self, package_id: str) -> Package | None:
        return self.packages.get(package_id)

    def get_packages(self) -> tuple[Package, ...]:
        return tuple(self.packages.values())
