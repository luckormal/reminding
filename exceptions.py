def sumDigits(s):
    """Assumes s is a string
       Return the sum of the decimal digits in s
       For exmaplne, if s ins "a2b3c' it returns 5
    """
    try:
        return len(s)
    except (ValueError, TypeError): 
        print(s, 'is not a string')
        
# print(sumDigits(333))

def findAnEven(L):
    """Assumes L is a list of integers
       Returns the first even number in L
       Raise ValueError if L does not contain an even number"""

    for i in L:
        try:
            if i%2 == 0:
                return i
        except:
            print(i, 'is not a number')
    print('Even number not found')


print(findAnEven(['1d',5,3]))
