n=int(input("Enter the number:"))
a,b=0,1
for i in range(n):
      print(a)
      # Suppose n = 5
      # Iteration 1: a=0, b=1 → print(0)
      # Iteration 2: a=1, b=1 → print(1)
      # Iteration 3: a=1, b=2 → print(1)
      # Iteration 4: a=2, b=3 → print(2)
      # Iteration 5: a=3, b=5 → print(3)
      a,b=b,a+b
  
