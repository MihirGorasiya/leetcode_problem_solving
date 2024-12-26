s = 'anagram'
t = 'nagaram'
chars = [*s]
for i in t:
    try:
        chars.remove(i)
    except:
        print('False')
print(len(chars))
print('True')