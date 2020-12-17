import math

if __name__ == "__main__":
    a=int(input())
    b=int(input())

    if not (1<=a<=math.pow(10,10) and 1<=b<=math.pow(10,10)):
        print("numbers should be greater than equal to 1 and less than equal to 10^10")
        exit()
    
    print(a+b)
    print(a-b)
    print(a*b)