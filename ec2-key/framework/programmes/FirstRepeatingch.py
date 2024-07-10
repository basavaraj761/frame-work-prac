s=input('enter the string:')

for index,ltr1 in enumerate(s):
    for ltr2 in s[index+1:]:
      if ltr1==ltr2:
          print(f'first repeated letter is {ltr1}')
