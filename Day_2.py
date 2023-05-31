import re
# check if word matches string
# description = "Kofi is the boy"
# match = re.search(r'in his shoes', description)
# if match:
#     print("YES", match.group())
# else:
#     print("No")

# check for a word in string
# description = "kofi is the boy"
# match = re.search(r'.', description)
# if match:
#     print("YES", match.group())
# else:
#     print("No")

# check for remaining word
# description = "Ama is good123"
# match = re.search(r'good\w\w', description)
# if match:
#     print("YES", match.group())
# else:
#     print("No")

# check for boundary
# description = "Ama is good123"
# match = re.search(r'\b i', description)
# if match:
#     print("YES", match.group())
# else:
#     print("No")

# check for white space
# description = "Ama is good123"
# match = re.search(r'\sis', description)
# if match:
#     print("YES", match.group())
# else:
#     print("No")

# check for non-whitespace
# description = "Ama is good123"
# match = re.search(r'\Sis', description)
# if match:
#     print("YES", match.group())
# else:
#     print("No")

# check for tab
# description = "Ama \tis good123"
# match = re.search(r'\tis', description)
# if match:
#     print("YES", match.group())
# else:
#     print("No")

# check for the period sign
# description = "Ama is \good123."
# match = re.search(r'\.', description)
# if match:
#     print("YES", match.group())
# else:
#     print("No")

# check for the backslash
# description = "Ama is \good123."
# match = re.search(r'\\', description)
# if match:
#     print("YES", match.group())
# else:
#     print("No")

# check for the first character in the string
# description = "Ama is \good123."
# match = re.search(r'^A', description)
# if match:
#     print("YES", match.group())
# else:
#     print("No")


# check for the last charaacter in the string
# description = "Ama is good123."
# match = re.search(r'.$', description)
# if match:
#     print("YES", match.group())
# else:
#     print("No")


# check for repeated character
# description = "Ama is good123."
# match = re.search(r'go+', description)
# if match:
#     print("YES", match.group())
# else:
#     print("No")

# description = "Ama is goodoooooo123."
# match = re.search(r'do+', description)
# if match:
#     print("YES", match.group())
# else:
#     print("No")


# description = "Ama is good123."
# match = re.search(r'..d+', description)
# if match:
#     print("YES", match.group())
# else:
#     print("No")


# to get the numbers
# description = "Ama is good123."
# match = re.search(r'\d\d\d', description)
# if match:
#     print("YES", match.group())
# else:
#     print("No")


# working with email

# email = "grace@gmail.com"

# check = re.search(r"\w@\w+", email)
# if check:
#     print("Yes", check.group())
# else:
#     print("No")



# email = "girl#@gmail.com"

# check = re.search(r"[\w#]+@[\w.]+", email)
# if check:
#     print("Yes", check.group())
# else:
#     print("No")

import re

regex_pattern = r"^(9|8|7)(\d{9})$"    # Do not delete 'r'.

a = int(input())

for _ in range(a):
    m = re.match(regex_pattern, input())
    if m: 
        print("YES") 
    else: 
        print("NO")




