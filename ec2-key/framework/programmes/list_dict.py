l1=['name','age','married']
l2=['basava',30,'not_yet']

d=zip
d = dict(zip(l1,l2))
print(d)

for i in d.items():
    print(i)