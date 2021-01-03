#armstrong number

num = int(input("Enter a number: "))

s = 0

y = num
while y > 0:
   digit = y % 10
   s += digit ** 3
   y//= 10

if num == s:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")