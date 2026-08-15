# this is used to write into a file, and if file exist then it will over write it, and if the file dosent exist it will create a new one...


k = open("ketan.txt", "w")

text = "Ketan is currently working on the new AI and machine learning Project..."

k.write(text)

k.close()