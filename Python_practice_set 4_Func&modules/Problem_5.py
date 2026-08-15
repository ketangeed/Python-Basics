# modules and pips - use external libraries..

# qs.1 import math module and use it to :
# 1. find the square root of 144.
# 2.calculate sine(90 degree). (hint. use math.radians())


# 1.
import math
print(math.sqrt(144))

# 2. 

import math
sine_value = math.sin(math.radians(90))
print(sine_value)



# pr 
import math
a = math.sqrt(144)
b = math.sin(math.radians(90))

print(a, b)




# qs.2 install and import the request module and fetch the data from "https://api.gthub.com"


import requests

r = requests.get("https://api.gthub.com")
print(r) # output = 200(ok) succeded
# to watch it use
print(r.text)
