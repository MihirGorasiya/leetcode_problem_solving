s = "5F3Z-2e-9-w"
k = 4

# s = "2-5g-3-J"
# k = 2

s = s.replace("-", "")
print(s)
l = len(s)
firstDash = l % k if l % k == 0 else k
i = 0
j = l - 1
ansFir = ""
ansSec = ""
answer = ""
dash = k

while i < j:
    if s[i] == "-":
        i = i + 1
    if s[j] == "-":
        j = j - 1
    if dash == 0:
        ansSec = ansSec + "-"
        ansFir = ansFir + "-"
        dash = k
    print(s[i])
    ansFir = ansFir + s[i].capitalize()
    ansSec = ansSec + s[j].capitalize()

    dash = dash - 1
    i = i + 1
    j = j - 1

print(ansFir.join(ansSec[::-1]))
