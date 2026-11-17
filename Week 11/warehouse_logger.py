import csv
import json
import os
import sys
from datetime import date

from package import Package


class WarehouseLogger:
    def __init__(self, id: str):
        self.id = id

    @staticmethod
    def _directory() -> str:
        return sys.path[0] or os.getcwd()

    def _state_filename(self) -> str:
        return f"{self.id}_state.json"

    def update_state(self, packages: dict[str, Package]) -> None:
        state = [package.convert_to_dict() for package in packages.values()]
        with open(
            os.path.join(self._directory(), self._state_filename()),
            "w",
            encoding="utf-8",
        ) as json_file:
            json.dump(state, json_file, indent=4)

    def parse_package_from_state_file(self, json_object: dict) -> Package:
        return Package(
            str(json_object["id"]),
            float(json_object["weight"]),
            float(json_object["travel_distance"]),
            date.fromisoformat(json_object["delivery_date"]),
        )

    def get_packages_from_state_file(
        self, state_file: str | None = None
    ) -> dict[str, Package]:
        filename = state_file or self._state_filename()
        try:
            with open(
                os.path.join(self._directory(), filename),
                encoding="utf-8",
            ) as json_file:
                json_objects = json.load(json_file)
        except FileNotFoundError:
            return {}

        return {
            package.id: package
            for package in (
                self.parse_package_from_state_file(json_object)
                for json_object in json_objects
            )
        }

    def get_packages_from_all_state_files(self) -> dict[str, Package]:
        packages = {}
        for filename in os.listdir(self._directory()):
            if filename.endswith("_state.json"):
                packages.update(self.get_packages_from_state_file(filename))
        return packages

    def generate_summary_per_date_file(
        self, packages: dict[date, tuple[Package, ...]]
    ) -> None:
        with open(
            os.path.join(self._directory(), "summary_per_date.csv"),
            "w",
            newline="",
            encoding="utf-8",
        ) as csv_file:
            writer = csv.writer(csv_file, delimiter=";")
            writer.writerow(("date", "num_packages", "fee"))
            for delivery_date in sorted(packages):
                packages_on_date = packages[delivery_date]
                fee = sum(
                    package.get_delivery_fee() for package in packages_on_date
                )
                writer.writerow(
                    (
                        delivery_date.isoformat(),
                        len(packages_on_date),
                        f"{fee:.2f}",
                    )
                )
