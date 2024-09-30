haystack = 'fsfsadbutsad'
needle = 'sad'

if haystack.__contains__(needle):
    print(haystack.index(needle))
else:
    print(-1)