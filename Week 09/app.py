from datetime import date

from package import Package
from warehouse import Warehouse


def run_application() -> None:
    warehouse = Warehouse()

    while True:
        choice = input(
            "[R] Register a new package"
            "[U] Update a package's destination"
            "[C] Cancel package delivery"
            "[V] View all packages in the warehouse"
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
            if warehouse.register_package(package):
                print(package.get_details())
            else:
                print("Could not register new package.")
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
        elif choice == "Q":
            break


if __name__ == "__main__":
    run_application()
