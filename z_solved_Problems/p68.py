"""
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
"""

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
answer = []

tempWords = []
tempWordsLen = 0

for word in words:
    if len(word) + tempWordsLen < maxWidth:
        tempWords.append(word)
        tempWordsLen += len(word) + 1
    else:
        print(tempWords)
        total_space = maxWidth // tempWordsLen
        print(total_space)

        tempWords = [word]
        tempWordsLen = len(word)


# tempString = ""
# for i in words:
#     if(len(tempString) + len(i)<maxWidth):
#         if(tempString != ""):
#             tempString = f"{tempString} {i}"
#         else:
#             tempString = f"{tempString}{i}"
#     else:
#         j = maxWidth-len(tempString)
#         k = len(tempString.split(" ")) - 1
#         x=""
#         # print(f"{tempString} _{(int(j/k)*" ")}_")
#         if(j > 0 and j%k==0):
#             l = ((int(j/k))*" ")
#             x = tempString.replace(" ", (int(j/k)*" "))
#         # else:


#         answer.append(x)
#         tempString = f"{i}"

# if(tempString!=""):
#     answer.append(f"{tempString}{(maxWidth-len(tempString))*' '}")

# print(answer)
