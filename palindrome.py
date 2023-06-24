def palindrome(s):
    return s[::-1] == s

while True:
    s = input("введите слово: ")
    if palindrome(s):
        print(f"{s} это слово является палиндромом")
    else:
        print(f"{s} это слово не является палиндромом")
