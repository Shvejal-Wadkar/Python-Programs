'''write a program which accept number from user and
check wheter that number is positive or Negative or Zero.'''


def Number(no):
	if no > 0:
		print("Number is possitive....")
	elif no == 0:
		print("zero")
	else: 
		print("Number is negative....")
		

def main():
	print("Enter the number: ")
	num = int(input())
	Ans = Number(num)

if __name__ == "__main__":
	main()