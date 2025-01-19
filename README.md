# dictionary_actions

> Dictionary actions is сonsist of three modules which perform various actions with the list data type.

#  1. How the keys_is_values works?       
> This code is a simple converter from list into dictionary. Every element from user's input convert into {key: value}
> pair which key and value is the same elements.

> [!NOTE]
> The function expects one argument which has type of data is list. Output of function will have type of dictionary.
 
# 2. How is rearrangement works?        
> This code counts the numbers of tuples of two numbers where their product would be equal to the same value
> obtained during multiplication.

> First block of for cycle is iterating variable and checking the same indices.
> If indices are equal, iteration is skipped, if not - two elements are multiplying and added into list.

> Second block of for cycle is iterating list ad if key not in dictionary, the key added into dictionary with value -1
> if key already in dictionary the value increase by +1.

> The third block of for cycle if iterating dictionary by its values and with operator += calculating amount of tuples
> with the same result of multiplications by combinatorics formula count * (count - 1) * 4.
   
> [!NOTE]
> The function expects one argument which has type of data is list. Output of function will have type of integer.
   
# 3. How is set_mismatch works?     
This code finds duplicate numbers and restores the order of the elements.

> Dictionary adds elements from list and counting them by length where the key is the elements counted in order,
> and their value is zero.

> In the next, cycle for iterating through nums variable and checking does dictionary have element by key. If True, the
> key increases by values.

> Next cycle for was wrapped in list comprehension and check doubling values in dictionary.
> After that, through the third for loop wrapped in a list, the comprehension iterates through the dictionary and
> finds a key whose value is zero. After this, index 0 is indicated because list comprehension was applied and in
> order not to add the entire list, then through index 0 we access the only element in the list and add only the
> element itself


> [!NOTE]
> The function expects one argument which has type of data is list. Output of function will have type of list.

> [!TIP]
> Example:       
> If variable has order: [1, 2, 2, 4]     
> Ouptut will be: [_, 2, 3, _]  

