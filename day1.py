inputs = open('./inputs/day2.txt', 'r').read().split('\n')

print(input.split('\n'))

elf_cal = 0
elfs_cals = []
for l in inputs:
    if l == "":
        elfs_cals.append(elf_cal)
        elf_cal = 0
    else: 
        elf_cal = elf_cal + int(l)

print(f'Max Cals - {max(elfs_cals)}')
elfs_cals.sort()
print(f'Max 3elf Cals - {sum(elfs_cals[-3:])}')
