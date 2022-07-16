import random

"""The goal of this code is to check an array and see if the sum of 2 of its element add up to a target
and if so, return their index in the array.
We create the array based on user input """

def finder(n):
    print('your array is : ' + str(n))
    res = [0]
    for i in range(len(n)):
        num = n[i]
        delta = target-num
        if delta > 0 and delta in n[i+1:]:
            res.append([n.index(n[i],i),n.index(delta,i+1)])
            res[0] += 1
    if res[0] > 0:
        return res
    else:
        print("There is no solution")
    
def rando(s,m):
    arr = []
    for _ in range(s):
        arr.append(random.randrange(1,m+1))
    return finder(arr)

size = int(input('What\'s the size of the array'))
max = int(input('What\'s the maximum int in the array'))
target = random.randrange(max/2,max)
print("the target is : " + str(target))
result = rando(size,max)
if (result != None):
    print(f"there is {str(result[0])} solution :")
    for i in range(1,result[0]+1):
        print(f"You can add the index {result[i][0]} and {result[i][1]}")
