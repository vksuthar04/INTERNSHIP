#Q3: https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

for k, c in groupby(input()):
    print("(%d, %d)" % (len(list(c)), int(k)), end=' ')