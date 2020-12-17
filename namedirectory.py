from operator import itemgetter

def person_lister(fun):
    def formatList(plist):
        plist.sort(key=itemgetter(2))
        newlist=[]
        for person in people:
            newlist.append(fun(person))
        return newlist
    return formatList

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')