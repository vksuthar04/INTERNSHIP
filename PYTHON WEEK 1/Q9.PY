#Q9: https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    x = [input().split() for i in range(n)]
    c = input()
    d = {}
    for i in range(n):
        d[x[i][0]] = list(map(float,x[i][1:]))
    print(f'{sum(d[c])/len(d[c]):.2f}')     
