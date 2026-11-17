from datetime import date


class Package:
    def __init__(
        self,
        id: str,
        weight: float,
        travel_distance: float,
        delivery_date: date,
    ):
        self.id = id
        self.weight = weight
        self.travel_distance = travel_distance
        self.delivery_date = delivery_date

    def get_delivery_fee(self) -> float:
        return round(0.50 + 0.08 * self.weight + 0.06 * self.travel_distance, 2)

    def get_details(self) -> str:
        return (
            f"Package(id={self.id}, weight={self.weight}, "
            f"travel_distance={self.travel_distance}, "
            f"delivery_date={self.delivery_date})"
        )

    def update_destination(self, new_distance: float) -> None:
        self.travel_distance = new_distance
