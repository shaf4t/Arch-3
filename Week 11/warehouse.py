from package import Package
from warehouse_logger import WarehouseLogger


class Warehouse:
    def __init__(self, id: str, capacity: int = 10):
        self.id = id
        self.capacity = capacity
        self.logger = WarehouseLogger(id)
        self.packages: dict[str, Package] = {}
        self.restore_state()

    def restore_state(self) -> None:
        self.packages = self.logger.get_packages_from_state_file()

    def _save_state(self) -> None:
        self.logger.update_state(self.packages)

    def register_package(self, package: Package) -> bool:
        if len(self.packages) >= self.capacity or package.id in self.packages:
            return False
        self.packages[package.id] = package
        self._save_state()
        return True

    def update_destination(self, package_id: str, new_distance: float) -> bool:
        package = self.packages.get(package_id)
        if package is None:
            return False
        package.update_destination(new_distance)
        self._save_state()
        return True

    def cancel_package(self, package_id: str) -> Package | None:
        package = self.packages.pop(package_id, None)
        if package is not None:
            self._save_state()
        return package

    def get_package(self, package_id: str) -> Package | None:
        return self.packages.get(package_id)

    def get_packages(self) -> tuple[Package, ...]:
        return tuple(self.packages.values())
