 #! Modules:

from math import * # importing everything from a built-in module
from random import randint # importing specific function

print("Floor of 8.9999 is", floor(8.9999))
print("Ceil of 9.0001 is", ceil(9.0001))
print("Random Number [1-100]:",randint(1, 100))

""" 
from test import Pout # importing function from other file
from test import take_list as listing # renaming the function for here
Pout("An outsider Function")
listing(1,3,5,7,9)
 """
""" 
# Installed PyAutoGUI from cmd "pip install pyautogui"
import pyautogui # it works despite having underline

for i in range(3):
    pyautogui.write('Py Spammer XD', interval=0.25)
    pyautogui.press('enter')
 """

 #! Exception Handling:
x = 10
try: # with try at least 1 of except or finally is required
    x //= 0
    print(x)
# if anything throws error here, will ignore try & go to except
except:
    print('Error Occured')
# won't come here if there're no errors in try
finally:
    print(x)
# will come here whether there's an error in try or not

print('End of Program')

"""
*Using this exception handling method (this is the absolute basics),
*even if some errors are found, the remaining correct code can run.
"""

 #! File:
# not working