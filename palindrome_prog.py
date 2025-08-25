n = input("Enter a word: ")  # Example input: madam
rev = ''  

for char in n:  
    rev = char + rev  

    # Iteration 1: char = 'm' → rev = 'm' + '' = 'm'
    # Iteration 2: char = 'a' → rev = 'a' + 'm' = 'am'
    # Iteration 3: char = 'd' → rev = 'd' + 'am' = 'dam'
    # Iteration 4: char = 'a' → rev = 'a' + 'dam' = 'adam'
    # Iteration 5: char = 'm' → rev = 'm' + 'adam' = 'madam'

if rev == n:  # 'madam' == 'madam' → Palindrome
    print("Palindrome")
else:
    print("Not a Palindrome")
