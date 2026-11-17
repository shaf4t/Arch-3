from datetime import date

from package import Package


class WarehouseLogger:
    LOG_FILE = "warehouse_log.txt"
    ACTIONS = {"register", "update", "cancel"}

    def __init__(self, id: str):
        self.id = id

    def log_action(self, action: str, package: Package) -> None:
        if action not in self.ACTIONS:
            raise ValueError(f"Unknown action: {action}")

        if action == "register":
            values = (
                self.id,
                action,
                package.id,
                str(package.weight),
                str(package.travel_distance),
                package.delivery_date.isoformat(),
            )
        elif action == "update":
            values = (self.id, action, package.id, str(package.travel_distance))
        else:
            values = (self.id, action, package.id)

        with open(self.LOG_FILE, "a") as log_file:
            log_file.write(";".join(values) + "\n")

    def parse_package_from_register_log_line(self, log_line: str) -> Package:
        values = log_line.strip().split(";")
        return Package(
            values[2],
            float(values[3]),
            float(values[4]),
            date.fromisoformat(values[5]),
        )

    def get_all_packages_from_log_file(
        self, only_current_warehouse: bool = True
    ) -> dict[str, Package]:
        packages = {}
        try:
            with open(self.LOG_FILE, "r") as log_file:
                log_lines = log_file.readlines()
        except FileNotFoundError:
            return packages

        for log_line in log_lines:
            values = log_line.strip().split(";")
            if len(values) < 2:
                continue
            warehouse_id, action, *action_values = values
            if only_current_warehouse and warehouse_id != self.id:
                continue

            if action == "register":
                package = self.parse_package_from_register_log_line(log_line)
                packages[package.id] = package
            elif action == "update" and len(action_values) >= 2:
                package = packages.get(action_values[0])
                if package is not None:
                    package.update_destination(float(action_values[1]))
            elif action == "cancel" and action_values:
                packages.pop(action_values[0], None)

        return packages
