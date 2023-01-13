#!/usr/bin/env python3


def is_lower(doms):
    if len(doms) == 0:
        return True
    # Return true if any doms in list < 3
    return any(d < 2 for d in doms)

count = 0
for i in range(0, 729):
    # Consider i as a base 3 number.
    zeros_place = i % 3
    three_place = (i // 3) % 3
    nine_place = (i // 9) % 3
    twenty_seven_place = (i // 27) % 3
    eighty_one_place = (i // 81) % 3
    two_forty_four_place = (i // 243) % 3

    left = []
    partner = []
    right = []

    def give(place_val, val):
        if place_val == 0:
            left.append(val)
        elif val == 1:
            partner.append(val)
        else:
            right.append(val)

    give(zeros_place, 0)
    give(three_place, 1)
    give(nine_place, 3)
    give(twenty_seven_place, 4)
    give(eighty_one_place, 5)
    give(two_forty_four_place, 6)

    if is_lower(left) and is_lower(right):
        count += 1

print(count)

print(count / 729)
