import string

# inputs = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw""".split('\n')
# 1st part - sum(points) = 157
# 2nd part - sum(points) = 70

inputs = open('./inputs/day3.txt', 'r').read().split('\n')


priority = {l:v+1 for v,l in 
    enumerate(string.ascii_lowercase + string.ascii_uppercase)}


inputs = [inputs[i:i+3] for i in range(0, len(inputs), 3)] #2nd part

points = []
for line in inputs:
    # 1st part - uncomment for 2nd part
    # a,b = line[:len(line)//2], line[len(line)//2:]
    # print(f"line = {line}, 1st part={a}, 2nd part={b}")
    # unique_chars = set(a).intersection(set(b))
    
    unique_chars = set.intersection(*list(map(set, line))) #2nd part
    print(f"unique_chars = {unique_chars}")
    points.append(priority.get(unique_chars.pop()))

print(sum(points))


