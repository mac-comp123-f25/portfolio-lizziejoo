import math


def class_calc(hour, hourthirty, nightclass, lab_three, lab_hourthirty, lab_hour):
    """
    A calculator that adds up all the hours of class that are attended in a week.
    Rules:
    - An hour-long class happens 3 times a week.
    - A 1.5-hour class happens 2 times a week.
    - A night class is once a week for 3 hours.
    - Labs can be 3, 1.5, or 1 hour long (assumed once a week each).
    """

    # Regular classes
    hourtotal = hour * 3  # each 1-hour class meets 3 times
    hourthirtytotal = hourthirty * 2  # each 1.5-hour class meets 2 times

    # Night class (once per week, 3 hours each)
    nightclasstotal = nightclass * 3

    # Labs (assumed weekly)
    lab_total = (lab_three * 3) + (lab_hourthirty * 1.5) + (lab_hour * 1)

    # Total weekly hours
    total = hourtotal + hourthirtytotal + nightclasstotal + lab_total

    return total

hour = int(input("How many 1-hour classes do you have? "))
hourthirty = int(input("How many 1.5-hour classes do you have? "))
nightclass = int(input("How many night classes (3 hrs each) do you have? "))
lab_three = int(input("How many 3-hour labs do you have? "))
lab_hourthirty = int(input("How many 1.5-hour labs do you have? "))
lab_hour = int(input("How many 1-hour labs do you have? "))


# Example usage:
weekly_hours = class_calc(hour, hourthirty, nightclass, lab_three, lab_hourthirty, lab_hour)
print("Total weekly class hours:", weekly_hours)