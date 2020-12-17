import re

if __name__ == "__main__":
    rows, columns =map(int, input().strip().split())
    matrix=[]
    for _ in range(rows):
        row = input()
        matrix.append(row)

    result=[]
    for col in range(columns):
        for row in range(rows):
            result.append(matrix[row][col])

    output="".join(result)
    x=re.sub('([a-zA-Z0-9])[^a-zA-Z0-9]+([a-zA-Z0-9])',r'\1 \2', output)
    x.replace('  ',' ')
    print(x)
