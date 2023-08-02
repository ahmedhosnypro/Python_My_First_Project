number = int(input())
ones = number % 10
tens = number // 10 % 10
thousands = number // 100
print(ones + tens + thousands)
