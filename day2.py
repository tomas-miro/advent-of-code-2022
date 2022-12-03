inputs = open('./inputs/day2.txt', 'r').read().split('\n')

# inputs = """A Y
# B X
# C Z"""

elf_mappping = {"A":"Rock", "B":"Paper", "C":"Scissor"}
my_mappping = {"X":"Rock", "Y":"Paper", "Z":"Scissor"}

rps_wins = {"Paper":"Rock", "Scissor":"Paper", "Rock":"Scissor"}
rps_loose = {v: k for k, v in rps_wins.items()} #inverts rps_wins


values = {"Rock":1, "Paper":2, "Scissor":3}
win = 6
draw = 3
lost = 0

#2nd round
two_my_mappping = {"X":lost, "Y":draw, "Z":win}

results = []
for line in inputs:
    e, m = line.split()
    e_play = elf_mappping[e]
    # 1st round
    # m_play = my_mappping[m]

    #2nd round
    print(f"{e_play} vs {m}")
    if two_my_mappping[m] == win:
        m_play = rps_loose[e_play]
    elif two_my_mappping[m] == lost:
       m_play = rps_wins[e_play]
    else:
        m_play = e_play

    print(f"{e_play} vs {m_play}")

    # score for play
    results.append(values[m_play])
    
    # tie
    if  e_play == m_play:
        print("I tie")
        results.append(draw)
    # lost 
    elif rps_wins[e_play] == m_play:
        print("I lost")
        results.append(lost)
   #win
    else:
        print("I win")
        results.append(win)
print(results)
print(sum(results))
