# s=input("enter the string")
#
# d={i:s.count(i) for i in s}
# print(d)


str="sheena loves eating apple and mango.her siater also loves eating apple and mango"
s1=str.split()
print(s1)

freq={i:s1.count(i) for i in s1}
print(freq)
