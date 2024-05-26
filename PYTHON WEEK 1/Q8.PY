#Q8: https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true

if __name__ == '__main__':

    n = int(input())

    Tuple1 = map(int, input().split())

    t = tuple(Tuple1)

    print(hash(t))

