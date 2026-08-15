#  there are two types of modules
# 1 = built in modules
# 2 = external modules
# import is the key word which helps to import the someones's else code.
# list of all built in modules : https://docs.python.org/3/py-modindex.html

import math
import mymodule
# if the function is not used then it shows the little blured color.

mymodule.hello() # we have made the function, here we can import it.
 

# print(math.sqrt[4])

# math is function, . means we want to use this module and sqrt is the function that is defined by user.




# can install/request for the external module in terminal.


import requests 
# it is the module to fetch the external https of the online pages.

r = requests.get("https://www.google.com")
print(r.text)
# text is an property.
#  now it'll see the google html program.
#  you always fetch the html code of any websites.