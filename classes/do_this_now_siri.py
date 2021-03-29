"""Do this now: Hey Siri, will it rain?
Given a list of rain chance percentages like:
[10, 0, 20, 50, 90]
If any of the chances are 50% or more then the answer is True."""


def main():
    rain_chances = [10, 0, 20, 50, 90]
    if is_going_to_rain(rain_chances):
        print("Yes, get an umbrella")
    else:
        print("No rain (Blind Melon)")


def is_going_to_rain(rain_chances):
    """Determine if it will rain or not based on rain chances."""
    [True for rain_chance in rain_chances if rain_chance >= 50]


main()
