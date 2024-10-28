# The code that takes the average of the desired number of words.

x = int(input("How many numbers will you average? :"))
# please enter integer

list = []

for i in range(x):
    a = float(input("your number:"))
    list.append(a)
    
y = sum(list)

print(f"the sum of the numbers you gave : {y}")
ortalama = y / x
print(f"average of the numbers you gave : {ortalama}") 
