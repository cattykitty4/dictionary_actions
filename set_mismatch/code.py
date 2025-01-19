def subsequenceCorrector(nums: [list]) -> [int]:
    dct = {i: 0 for i in range(1, len(nums) + 1)}
    for el in nums:
        dct[el] += 1

    lst = [key for key, value in dct.items() if value == 2]

    lst.append([key for key, value in dct.items() if value == 0][0])

    return lst

# This code finds duplicate numbers and restores the order of the elements.
# For example if variable has order [1, 2, 2, 4], output will be [_, 2, 3, _]

# How it works
# Dictionary adds elements from list and counting them by length where the key is the elements counted in order,
# and their value is zero.

# In the next, cycle for iterating through nums variable and checking does dictionary have element by key. If True, the
# key increases by values.

# Next cycle for was wrapped in list comprehension and check doubling values in dictionary.
# After that, through the third for loop wrapped in a list, the comprehension iterates through the dictionary and
# finds a key whose value is zero. After this, index 0 is indicated because list comprehension was applied and in
# order not to add the entire list, then through index 0 we access the only element in the list and add only the
# element itself
