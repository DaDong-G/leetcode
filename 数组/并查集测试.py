d = [0] * 4
for i in range(4):
    d[i] = i
print(d)



def find( x):
    if d[x] == x:
        print(x)
        return x
    else:
        print(1111111111,d[x])
        return find(d[x])


def merge( i,  j):

    d[find(i)] = find(j)
    print(d)

# find(1)

merge(1,2)

find(1)