if __name__ == "__main__":
    m=int(input())
    list1=map(int, input().split())
    

    n=int(input())
    list2=map(int, input().split())
    
    a=set(list1)
    b=set(list2)

    if (len(a) < m) or (len(b) < n):
        print("set is incomplete")
        exit()

    result = a.symmetric_difference(b) 
    for i in result:
        print(i)