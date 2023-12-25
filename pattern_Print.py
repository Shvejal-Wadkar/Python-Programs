'''write a program which accept number from user 
and print that number of "*" on screen.
ex. input-5    output-* * * * *'''

def Star(num):
	i = 1
	while i <=num :
		print("*")

		i = i+1


def main():
	print("Enter the Number: ")
	no = int(input())

	Ans = Star(no)


if __name__ == "__main__":
	main()