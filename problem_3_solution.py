
with open('problem_3_names.txt') as f:
    names = f.readlines()
    
names_2 = [i for i in names if i != '\n']

names_3 = sorted(names_2, key = lambda x: x.split(' ')[-1])

names_4 = []

for i in range(1, 101):
    names_4.append(f'{i}. {names_3[i-1]}')
    
names_5 = names_4[:-5]

with open('problem_3_names_output.txt', 'w') as f:
    f.writelines(names_5)