#Q7:https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true

for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(int(a//b))
    except Exception as e:
        print("Error Code:",e)