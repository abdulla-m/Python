if __name__ == "__main__":
    a=int(input())    
    b=int(input())    
    m=int(input())

    if not ( 1<=a<=10 and 1<=b<=10 and 2<=m<=1000):
        print("number are not in range");
        exit()

    print(a**b)
    print((a**b)%m)