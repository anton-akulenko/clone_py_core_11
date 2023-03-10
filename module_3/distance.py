import math

RADIUS: float = 6371.01


def distance_between_cities(lat1, lon1, lat2=51.5072, lon2=-0.1275) -> float:
    def calculate_distance():
        nonlocal lat1, lon1, lat2, lon2
        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)

        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)

        distance = RADIUS * math.acos(math.sin(lat1) * math.sin(lat2) +
                                      math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))
        return distance

    result = calculate_distance()
    return result


def baz():
    pass


print(__name__)
if __name__ == "__main__":
    distance = distance_between_cities(50.45, 30.523, lon2=1275)
    print(distance)