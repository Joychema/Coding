# A palindrome is a string that can be equally read from left to right or
# right to left, omitting blank spaces, and ignoring capitalization.

def isPalindrome(word):
    return word == word[::-1]

text = isPalindrome("helo")
print(text)

txt = isPalindrome("madam")
print(txt)

