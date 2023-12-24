'''write a program which contains one function that
accept one number from user and returns true
if number is divisible by 5 otherwise return false.'''


def Divisible(value):
	if value%5 == 0:
		print("treu")
	else:
		print("false")


def main():

	print("enter the number: ")
	num = int(input())

	Ans = Divisible(num)



if __name__ == "__main__":
	main()