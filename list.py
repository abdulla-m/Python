if __name__ == "__main__":
    n=int(input())

    mylist=[]
    commands=[]
    while(n>0):
        commands.append(input())
        n -=1

    for cmd in commands:
        if  cmd.find("insert") > -1:
            insertcmd=cmd.split(" ")
            if not insertcmd[2].isnumeric():
                print("number to be added should be numeric")
                exit()
            index=int(insertcmd[1])
            num=int(insertcmd[2])
            mylist.insert(index,num)
        if cmd.find("print") > -1:
            print(mylist)
        if cmd.find("reverse") > -1:
            mylist.reverse()
        if cmd.find("remove") > -1:
            rmcmd=cmd.split(" ")
            num=int(rmcmd[1])
            mylist.remove(num)
        if cmd.find("append") > -1:
            appcmd=cmd.split(" ")
            num=int(appcmd[1])
            mylist.append(num)
        if cmd.find("sort") > -1:
            mylist.sort()
        if cmd.find("pop") > -1 :
            mylist.pop(len(mylist)-1)
            