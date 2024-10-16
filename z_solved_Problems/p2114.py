sentences = ["alice and bob love leetcode",
             "i think so too", "this is great thanks very much"]

sentences = ["please wait", "continue to fight", "continue to win"]

answer = 0
for i in sentences:
    count = i.count(' ') + 1
    answer = max(count, answer)
    

print(answer)
