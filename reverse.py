def reverse(x: int) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    rev = 0
    sign = -1 if x < 0 else 1
    n = abs(x)  
    while n != 0:
        digit = n % 10
        n //= 10
        # check overflow before multiplying
        if rev > (INT_MAX - digit) // 10:
            return 0
        rev = rev * 10 + digit
    return sign * rev
# Test cases
print("Input: 123   -> Output:", reverse(123))        
print("Input: -123  -> Output:", reverse(-123))       
print("Input: 120   -> Output:", reverse(120))        
print("Input: 1534236469 -> Output:", reverse(1534236469))  


    
