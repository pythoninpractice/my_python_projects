

def is_2025_number(num):
    num_str = str(num)
    for i in range(1, len(num_str)):
        left = num_str[:i]
        right = num_str[i:]
        print(left)
        print(right)
        print((int(left) + int(right))**2)
        print(str(int(left)) + str(int(right)))
        if str((int(left) + int(right))**2) == str(int(left)) + str(int(right)):
            return True
    return False
    
def is_2025_number_2(num):
    num_str = str(num)
    x = int(len(num_str)/2)
    if (int(num_str[:x]) + int(num_str[x:]))**2 == num:
            return True
    return False
    
    
print('results for 52: ', is_2025_number(52)) 
print('results for 81: ', is_2025_number(81))       
print('results for 3025: ', is_2025_number(3025)) 
print('results for 9081: ', is_2025_number(9801))
print('results for 8001: ', is_2025_number(8001))
        
'''
nums = []

for k in range(8000, 8010):
    if is_2025_number(k):
        nums.append(k)
        
print('Total of T(4): ', nums)
'''