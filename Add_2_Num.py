''' write a program which contains 
one function named as Add() 
which accept two numbers from user and 
return addition of that two numbers'''


def Add(num1,num2):
	Addition = num1 + num2
	return Addition

def main():
	print("Enter first number: ")
	no1 = int(input())

	print("Enter second number: ")
	no2 = int(input())

	Ans = Add(no1,no2)
	print("Addition is: ",Ans)

if __name__ =="__main__":
	main()
