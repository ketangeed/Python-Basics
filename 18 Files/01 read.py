# this is used to read an existing file, and if the file is not present it will just throw an error...
# use "with" method always for the files, it will close the file by default..
# use this most of the timess..


f = open("ketan.txt", "r")

content = f.read()

print(content)

f.close()