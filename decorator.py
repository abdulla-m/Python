def mydecorator(f):
    def fun(l):
        for i in range(len(l)):
            p=l[i]
            print(p)
            if len(p) == 10:
                l[i] = "+91 " + p[0:5] + " " + p[5:]
            if p.startswith("0") and len(p) == 11:
                p = p[1:]
                l[i] = "+91 " + p[0:5] + " " + p[5:]
            if p.startswith("91") and len(p) == 12:
                l[i] = "+" + p[0:2] + " " + p[2:7] +" "+p[7:]
            if p.startswith("+91"):
                l[i] = p[0:3] + " " + p[3:8] +" "+p[8:]
        f(l)
    return fun

@mydecorator
def sort_phone(l):
    print(*sorted(l),sep="\n")

if __name__ == "__main__":
    l = [input() for _ in range(int(input()))]
    sort_phone(l)