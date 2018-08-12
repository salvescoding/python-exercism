room_mates = {
    'Sergio': 60,
    'Marise': 60,
    'Erika': 35,
    'Floriane': 26
}
totals = {
    'Sergio': 0,
    'Marise': 0,
    'Erika': 0,
    'Floriane': 0
}

days = 60
bill = 52.89


def bill_per_day():
    """ Calculate bill per day """
    return round(bill / 60, 3)

def calculate_value_to_add(days_to_calc):
    """ Returns the value to add on each roommate on the days to be calculated.

        Arguments: Days to calculate
    """
    return round((bill_per_day()*days_to_calc) / len(room_mates), 2)


def get_roommate_with_lowest_days():
    """ Returns a tuple with the key and value, with the lowest value from the dict """
    return min(room_mates.items(), key=lambda x: x[1])


def remove_roommate_from_dict(roommate):
    """ Removes the roommate from the original dictionary, returns None if not found.

        Arguments: The roommate as a string.
    """
    room_mates.pop(roommate, None)

def add_value_to_each_roommate(value_to_add, days_to_calc):
    """ Adds the value to each roommate of the totals dictionary """
    for key in room_mates:
        totals[key] += value_to_add
        room_mates[key] -= days_to_calc


while days > 0:
    person, days_to_calc = get_roommate_with_lowest_days()
    value_to_add = calculate_value_to_add(days_to_calc)
    add_value_to_each_roommate(value_to_add, days_to_calc)
    remove_roommate_from_dict(person)
    days -= days_to_calc

print(totals)

