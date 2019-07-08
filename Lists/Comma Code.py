
def listValues(spam):
    ans=""
    for i in range(len(spam)-1):
        ans += spam[i] + ", "
    ans+= "and " + spam[-1]
    return ans

spam = [ 'apples', 'bananas', 'tofu', 'cats']

print(listValues(spam))
