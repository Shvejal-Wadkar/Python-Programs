'''write a program which display
first 10 even number on screen'''


def main():

	for number in range(1, 22):
		if number % 2 ==0:
			print(number)

if __name__ == "__main__":
	main()