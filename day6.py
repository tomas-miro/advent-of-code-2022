# inputs = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb",
#         "bvwbjplbgvbhsrlpgdmjqwftvncz",
# "nppdvjthqldpwncqszvftbrmjlhg",
# "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 
# "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]
# ex_sols = [7,5,6,10,11]

inputs = open('./inputs/day6.txt', 'r').read().split('\n')

sols = []
#cut_off = 4 #1st part
cut_off = 14 #2nd part

for i in inputs:  
    for l in range(len(i)):
        packet = i[l:l+cut_off]
        if len(set(packet)) == cut_off:
            sols.append(l+cut_off)
            break
print(sols)
