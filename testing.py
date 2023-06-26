
def power_func(b, pows):
    ans = b
    while pows > 1:
        ans = ans * b
        pows = pows - 1
    return ans


print("Enter the base value: ")
or_base = int(input())
print("Enter the power value: ")
p = int(input())
print("Enter the divisor: ")
divisor = int(input())

binary = format(p, 'b') #converting the power to binary format
#converting the binary to a list of the values then converting the 'char' elements to 'int'
values = [int(x) for x in binary]
#reversing the list order
values.reverse()
final = []

x = 1
for i in values:
    if i == 1:
        base = (power_func(or_base, x)) % divisor
        #adding the modulo values to a new array
        final.append(base)
    x = x * 2
product = 1
comp = 0
while comp < len(final):
    #multiplying all modulo values
    product = product * final[comp]
    comp = comp + 1
mod = product % divisor
print("The modulo value is: " + str(mod))


