# used to close the file automatically.
# always use the with statement in big projects

with open("ketan.txt", "r") as f:
    content = f.read()
    print(content)

# now no need to close the file with f.close..
# bcoz it is already closed by deafault..