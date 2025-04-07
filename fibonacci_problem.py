
import json

fib = [1,1]
while fib[-1] < 10**100:
    fib.append(fib[-2] + fib[-1])
    
def sum_is_even(num):
    s = list(str(num))
    s = sum([int(i) for i in s])
    return s%2 == 0
    

    
fib_2 = [i for i in fib if sum_is_even(i)]

print(fib_2)

print(len(fib_2))

def count_is_even(num):
    s = len(str(num))
    return s%2 == 0
    
fib_3 = [i for i in fib_2 if count_is_even(i)]

print(fib_3)

print(len(fib_3))

def prod_of_split(num):
    s = str(num)
    left = str(num)[:int(len(s)/2)]
    right = str(num)[int(len(s)/2):]
    return int(left) * int(right)
    
fib_4 = [prod_of_split(i) for i in fib_3]

print(fib_4)
print(len(fib_4))


with open('result.json', 'w') as f:
    json.dump(fib_4, f)