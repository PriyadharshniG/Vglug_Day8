n = int(input("Enter a number: "))  # Example input: 153
num = n
order = len(str(n))  
sum = 0  # Initially sum = 0

while num > 0:  # num = 153 > 0 --> Iteration 1, then num=15 > 0 --> Iteration 2, then num=1 > 0 --> Iteration 3
    digit = num % 10  
    
    # Iteration 1: digit = 153 % 10 = 3
    # Iteration 2: digit = 15 % 10 = 5
    # Iteration 3: digit = 1 % 10 = 1

    sum += digit ** order  
    
    # Iteration 1: sum_of_digits = 0 + 3**3 = 27
    # Iteration 2: sum_of_digits = 27 + 5**3 = 27 + 125 = 152
    # Iteration 3: sum_of_digits = 152 + 1**3 = 152 + 1 = 153

    num //= 10  
    
    # Iteration 1: num = 153 // 10 = 15
    # Iteration 2: num = 15 // 10 = 1
    # Iteration 3: num = 1 // 10 = 0 --> loop ends

if sum == n:  # 153 == 153 → True
    print("Armstrong")
else:
    print("Not an Armstrong")
