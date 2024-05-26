#Q2: https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    # Calculate sum
    sum_result = a + b
    
    # Calculate difference
    diff_result = a - b
    
    # Calculate product
    product_result = a * b
    
    # Print results
    print(sum_result)
    print(diff_result)
    print(product_result)

    x,y,z=a+b,a-b,a*b
    print(x,y,z)