import math

def calculate_formaula(a,b,c,d):
    first=1
    second=1
    for i in range(0,b):
        first = a*first
    for i in range(0,d):
        second = c*second
    
    print(first)
    print(second)
    return first + second


if __name__ == "__main__":
    a = int(input("Enter A:"))
    b = int(input("Enter B:"))
    c = int(input("Enter C:"))
    d = int(input("Enter D:"))
    
    if not (1 <= a <= 1000 and 1<=b<=1000 and 1<=c<=1000 and 1<=d<=1000):
       print("values should be less greater to 1 & less equal to 1000 ") 
       exit()

    print(calculate_formaula(a,b,c,d))    