def combinator(nums: [list]) -> int:
    counter = 0
    container = []
    dct = {}

    for idx, el in enumerate(nums):
        for i, number in enumerate(nums):
            if nums[idx] != nums[i]:
                multiplication = number * el
                container.append(multiplication)

    for key in container:
        if key not in dct:
            dct[key] = -1
        else:
            dct[key] += 1

    for value in dct.values():
        counter += value * (value - 1) * 4

    return counter


# This code counts the numbers of tuples of two numbers where their product would be equal to the same value
# obtained during multiplication.

# How it works
# First block of for cycle is iterating variable and checking the same indices.
# If indices are equal, iteration is skipped, if not - two elements are multiplying and added into list

# Second block of for cycle is iterating list ad if key not in dictionary, the key added into dictionary with value -1
# if key already in dictionary the value increase by +1

# The third block of for cycle if iterating dictionary by its values and with operator += calculating amount of tuples
# with the same result of multiplications by combinatorics formula count * (count - 1) * 4

