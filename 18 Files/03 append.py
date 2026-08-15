#  this is used to add anything to the file is it exist and if the file is not present then it will create a new file...


g = open("ketan.txt", "a")

string = "Ketan is currently studing the python..."

g.write(string)

g.close()