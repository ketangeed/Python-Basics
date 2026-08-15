import requests

r = requests.get('https://api.github.com/users/codewithharry')
# so we are saying go here and fetch the content of this URL..

print(r.text)

# OR 

# to create the file of the info

with open("codewithharry.txt", "w") as w :
    w.write(r.text)