def mutate_string(string,index, character):
    mylist = list(string)
    mylist.insert(index,character)
    return "".join(mylist)

if __name__ == "__main__":
    string=input()
    i, c=input().split()
    print(mutate_string(string,int(i),c))

