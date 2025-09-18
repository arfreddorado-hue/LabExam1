def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

while True:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        print("Invalid integer")
        continue
    x = a

    b = int(input("Enter another positive integer: "))
    if b <= 0:
        print("Invalid integer!!")
        continue
    y = b

    if x > 0 and y > 0:
        break

print(f"The LCM of {x} and {y} is = {lcm(x, y)}")
