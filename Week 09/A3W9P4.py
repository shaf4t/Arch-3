class Converter:
    _METERS_PER_UNIT = {
        "inches": 0.0254,
        "feet": 0.3048,
        "yards": 0.9144,
        "miles": 1609.344,
        "kilometers": 1000,
        "meters": 1,
        "centimeters": 0.01,
        "millimeters": 0.001,
    }

    def __init__(self, length, unit):
        if unit not in self._METERS_PER_UNIT:
            raise ValueError(f"Unsupported unit: {unit}")

        self.length = length * self._METERS_PER_UNIT[unit]

    def _convert_to(self, unit):
        return self.length / self._METERS_PER_UNIT[unit]

    def inches(self):
        return self._convert_to("inches")

    def feet(self):
        return self._convert_to("feet")

    def yards(self):
        return self._convert_to("yards")

    def miles(self):
        return self._convert_to("miles")

    def kilometers(self):
        return self._convert_to("kilometers")

    def meters(self):
        return self._convert_to("meters")

    def centimeters(self):
        return self._convert_to("centimeters")

    def millimeters(self):
        return self._convert_to("millimeters")


if __name__ == "__main__":
    pass