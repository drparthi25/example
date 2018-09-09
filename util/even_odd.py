def swap(x,y):
    a=x
    b=y
    return b,a

a = [1, 2, 6, 3, 4, 9, 44, 55, 88, 99, 222]
#even_list = dict([(i,j) for i,j in enumerate(a) if i%2 == 0])
#odd_list = dict([(i,j) for i,j in enumerate(a) if i%2 != 0])
even_index = []
even_number = []
odd_index = []
odd_number = []
for i,j in enumerate(a):
    if j%2 == 0:
        even_number.append(j)
        even_index.append(i)
    else:
        odd_number.append(j)
        odd_index.append(i)
moving_even = []
moving_odd = []
for i in range(len(even_index)):
    if i not in even_index:
        moving_even.append(i)

for k in range(len(even_index),len(a)):
    if k not in odd_index:
        moving_odd.append(k)

print "master list",a
for i in range(len(moving_odd)):
    a[moving_even[i]],a[moving_odd[i]] = swap(int(a[moving_even[i]]),int(a[moving_odd[i]]))
print "even moved to left and odd moved to right",a


        
    
