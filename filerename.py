import os
path = input("Indiquez le chemin du dossier: ")

for file in os.listdir(path):
	os.rename(path + "/" + file, path + "/" + file[0:5] + ".jpg")
