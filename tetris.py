import math

def biorhythm(days_alive, physical_period, emotional_period, intellectual_period):
    """Calculate the biorhythm for a person given the number of days they have been alive.
    days_alive: The number of days the person has been alive.
    physical_period: The period of the physical biorhythm in days.
    emotional_period: The period of the emotional biorhythm in days.
    intellectual_period: The period of the intellectual biorhythm in days.
    """
    sin_physical = math.sin(2 * math.pi * days_alive / physical_period)
    sin_emotional = math.sin(2 * math.pi * days_alive / emotional_period)
    sin_intellectual = math.sin(2 * math.pi * days_alive / intellectual_period)
    return (sin_physical, sin_emotional, sin_intellectual)

print(biorhythm(100, 23, 28, 33))