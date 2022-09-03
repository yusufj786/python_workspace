# python program to check whether string ispalindrome or not
from re import S

def isPalindrome(s):
    rev = ''.join(reversed(s))
    if (s == rev):
        return True
    return False
    s = "malayalam"
ans = isPalindrome(S)

if (ans):
    print("Yes")
else:
    print("No")