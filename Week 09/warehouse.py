from package import Package


class Warehouse:
    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        self.packages: dict[str, Package] = {}

    def register_package(self, package: Package) -> bool:
        if len(self.packages) >= self.capacity or package.id in self.packages:
            return False

        self.packages[package.id] = package
        return True

    def update_destination(self, package_id: str, new_distance: float) -> bool:
        package = self.packages.get(package_id)
        if package is None:
            return False

        package.update_destination(new_distance)
        return True

    def cancel_package(self, package_id: str) -> Package | None:
        return self.packages.pop(package_id, None)

    def get_package(self, package_id: str) -> Package | None:
        return self.packages.get(package_id)

    def get_packages(self) -> tuple[Package, ...]:
        return tuple(self.packages.values())
