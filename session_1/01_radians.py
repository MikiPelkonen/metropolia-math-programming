import numpy as np


def degrees_to_radians(degrees: float) -> float:
    return np.deg2rad(degrees)


def radians_to_degrees(radians: float) -> float:
    return np.rad2deg(radians)


# Excercise 1.
RADIANS: tuple[float, float] = (2.493, 0.911)
DEGREES: tuple[float, float] = (137.7, 62.3)

print("--- Exercise set 1 ---")
for radian in RADIANS:
    print(f"{radians_to_degrees(radian):.1f}°")
print()
for degree in DEGREES:
    print(f"{degrees_to_radians(degree):.2f} rad")
print()
array_degrees = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])
array_radians = np.deg2rad(array_degrees)

for deg, rad in zip(array_degrees, array_radians):
    print(f"{deg:>6.1f}°    ->{rad:>8.2f} radians")
