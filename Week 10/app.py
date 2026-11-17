from datetime import date

from package import Package
from warehouse import Warehouse
from warehouse_manager import WarehouseManager


def run_application() -> None:
    warehouse = Warehouse("Beurs")
    manager = WarehouseManager()

    while True:
        choice = input(
            "[R] Register a new package"
            "[U] Update a package's destination"
            "[C] Cancel package delivery"
            "[V] View all packages in the warehouse"
            "[F] Get total fee between two dates"
            "[Q] Quit\n"
            "Input your choice: "
        ).upper()

        if choice == "R":
            package_data = input(
                "Enter package details (id,weight,distance,delivery date): "
            ).split(",")
            package = Package(
                package_data[0],
                float(package_data[1]),
                float(package_data[2]),
                date.fromisoformat(package_data[3]),
            )
            if manager.stores_package_id(package.id) or not warehouse.register_package(
                package
            ):
                print("Could not register new package.")
            else:
                print(package.get_details())
        elif choice == "U":
            package_id, distance = input(
                "Enter package ID and new distance: "
            ).split(",")
            if warehouse.update_destination(package_id, float(distance)):
                package = warehouse.get_package(package_id)
                if package is not None:
                    print(package.get_details())
            else:
                print("Could not update the package.")
        elif choice == "C":
            package = warehouse.cancel_package(input("Enter package ID: "))
            if package is not None:
                print(package.get_details())
            else:
                print("Could not cancel the package.")
        elif choice == "V":
            packages = warehouse.get_packages()
            if packages:
                for package in packages:
                    print(package.get_details())
            else:
                print("This warehouse is empty.")
        elif choice == "F":
            from_date, to_date = input(
                "Enter the date range (from,to): "
            ).split(",")
            from_date = date.fromisoformat(from_date)
            to_date = date.fromisoformat(to_date)
            if from_date > to_date:
                print("Could not calculate the total fee.")
            else:
                total_fee = manager.get_total_fee_by_range(from_date, to_date)
                print(f"Collected fees: {total_fee:.2f} EUR")
        elif choice == "Q":
            break


if __name__ == "__main__":
    run_application()
