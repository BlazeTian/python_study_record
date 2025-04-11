""""
题目8：
判断字符串是否回文
"""
def is_palindrome(s):
    if s == s[::-1]:
        print("该字符串是回文")
    else:
        print("该字符串不是回文")


if __name__ == '__main__':
    is_palindrome("abcba")