import os

print("Hello world")

def tictactoe():
	pass

def menu():

	a = True

	os.system('clear')
	print("\n Please make your selection :")
	print("\n ")
	print("\n 0 : Continue")
	print("\n 1 : Tic-Tac-Toe")
	print("\n 2 : Exit")

	a = input("make your selection")
	
	if a =="2":
		b=False
	else:
		if b == 1:
			tictactoe()

	return b


flag = True

while flag :
	flag=menu()
	