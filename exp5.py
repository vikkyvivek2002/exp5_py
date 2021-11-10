n = int(input('Enter number: '))
t = n
sum = 0
while n:
    sum += n%10
    n //= 10
if t%sum == 0:
    print('%d is Harshad Number' % (t))
else:
    print('%d is Not Harshad Number' % (t))
