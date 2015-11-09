from collections import Counter
import string
def swapchars(myString):
    (a,b) = Counter(myString).most_common(1)[0]
    (c,d) = Counter(myString).most_common(99)[-1]
    if a == " ":
        (a,b) = Counter(myString).most_common(2)[1]
    myString = string.replace(myString, c, '0')
    myString = string.replace(myString, a, c)
    myString = string.replace(myString, '0', a)
    print myString

swapchars("I\'m just a chi-town coder with a nice flow.")
