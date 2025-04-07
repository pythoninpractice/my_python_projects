
all_numbers = list(range(2000))

multiples_of_3_or_5 = []

for i in all_numbers:
    if i % 3 == 0 or i % 5 == 0:
        multiples_of_3_or_5.append(i)
        
        
total_1 = sum(multiples_of_3_or_5)

total_2 = sum([i for i in all_numbers if i % 3 == 0 or i % 5 == 0])

print('total_1: ', total_1)

print('total_2: ', total_2)