import os

print("Hello world")

def menu():

	os.system('clear')
	print("\n Please make your selection :")
	print("\n ")
	print("\n 0 : Continue")
	print("\n 1 : Exit")

	a = input("make your selection")
	if a == "0":
		b=True
	elif a =="1":
		b=False
	else:
		b=True

	return b


flag = True

while flag :
	flag=menu()
	