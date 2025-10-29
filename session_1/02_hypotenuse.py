import numpy as np

LEGS: tuple[float, float] = (1.6, 2.3)

hypotenuse = np.hypot(LEGS[0], LEGS[1])
print(
    f"The hypotenuse of a right-angled triangle with legs of {LEGS} is {hypotenuse:.2f}."
)
