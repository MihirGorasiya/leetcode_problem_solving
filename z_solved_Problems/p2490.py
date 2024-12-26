sentence = "leetcode exercises sound delightful"
sentence = "Leetcode is cool"

for i in range(len(sentence)):
    if sentence[i] == " " and sentence[i - 1] != sentence[i + 1]:
        print("False")

print(sentence[0] == sentence[-1])
