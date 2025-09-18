def palindrome(pal):
    return pal == pal[::-1]

def to_binary(num):
    if num.isDigit():
        return bin(int(num))[2:1]
    return None
value = input("Enter a value: ")
palNum = palindrome(value)
print("Input is a palindrome " + palNum)

bina = to_binary(value)

if bina:
    print("Binary is equiuvalent: " + bina)
    binapal = palindrome(bina)
    print("Binary is palindrome " + binapal)
else:
    print("No binary input")