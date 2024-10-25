n = 2


def isBadVersion(version):
    bad = 2
    
    return version >= bad


first = 1

mid = (first + n) // 2
while first <= n:
    mid = (first + n) // 2
    print(f"{mid} {first} {n}")
    if isBadVersion(mid):
        n = mid-1
        if not isBadVersion(mid-1):
            break
    else:
        first = mid+1

print(mid)
