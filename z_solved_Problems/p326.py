n = 27

def isPowerOfThree(n):
        if n == 1:
            return True
        elif n <=0 or n%3!=0:
            return False
        else:
            return isPowerOfThree(n//3)
        
print(isPowerOfThree(n))