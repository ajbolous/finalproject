def multiply(A, B):
    
    minlen = min(len(A), len(B))
    carry = 0
    result = ""
    for i in range(1,minlen+1):
        a = A[minlen - i]
        b = B[minlen - i]
        res = (ord(a)- ord('0'))*( ord(b)- ord('0')) + carry
        c = res%10
        carry = res/10
        c += ord('0')
        result = chr(c) + result
        print result
    return result



multiply('10','12')