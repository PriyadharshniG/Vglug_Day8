s1=input("enter s1:")
s2=input("enter s2:")
res=""
for char in s1:
    if char in s2:
        res+=char
if res==s1:
    print("True")
else:
    print("False")
        
