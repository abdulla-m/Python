
def say_hello(f):
    def say(s):
        print("hello "+s)
    return say

@say_hello
def print_me(s):
    print(s)

if __name__ == "__main__":
    print_me(input())