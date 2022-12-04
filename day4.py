# inputs = """2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8""".split('\n')
# 1st part - counter = 2
# 2nd part - counter = 4

inputs = open('./inputs/day4.txt', 'r').read().split('\n')

counter_pt1 = 0
counter_pt2 = 0
for l in inputs:
    a, b = l.split(',')
    r_a = set(range(int(a.split('-')[0]), int(a.split('-')[1])+1))
    r_b = set(range(int(b.split('-')[0]), int(b.split('-')[1])+1))
    
    #1st part
    if r_a.issubset(r_b) or r_b.issubset(r_a):
        print(f"{l} r_a issubset {r_a.issubset(r_b)} r_b contains {r_b.issubset(r_a)}")
        counter_pt1 += 1

    #2nd part 
    if r_a.intersection(r_b) :
        counter_pt2 += 1

print(f"{counter_pt1=}")
print(f"{counter_pt2=}")


