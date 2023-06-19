x = 1
print("Enter the base value: ")
base = int(input())
print("Enter the power value: ")
p = int(input())
print("Enter the modulo value: ")
modulo = int(input())
ans = base
while p > 1:
    ans = ans * base
    p = p - 1
answer = ans % modulo

print(answer)
