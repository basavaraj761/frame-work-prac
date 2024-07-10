n = int(input('enter the number:'))
ori_n = n
rev = 0
while n != 0:
    rev = rev * 10 + (n % 10)
    n = n // 10

print(rev)
if rev == ori_n:
    print(ori_n, ' is palindrome')
else:
    print(ori_n,'not palindrome')
