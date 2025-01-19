def listConverter(user: [list]) -> [dict]:
    dct = {}
    return {element: dct.get(element, element) for element in user}

# This code is a simple converter from list into dictionary. Every element from user's input convert into {key: value}
# pair which key and value is the same elements.
