''' write a program which contains one function named as ChkNum()
which accept one parameter as number. If number is even then
it should display "Even Numbe" otherwise display "Odd Number" on console'''


def ChkNum(num):
    if num%2==0:

        print("number is even")
    else:
        print("number is odd")
        return num

def main():
    
    print("Enter one number: ")
    no1 = int(input())

    Ans=ChkNum(no1)

if __name__ == '__main__':
    main()
