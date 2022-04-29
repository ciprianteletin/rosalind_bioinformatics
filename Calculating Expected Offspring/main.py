input = '17976 17868 16250 16148 18134 17357'
list = [int(i) for i in input.split(' ')]

result = list[0] * 2 + list[1] * 2 + list[2] * 2 + list[3] * 2 * 3.0 / 4 + list[4] * 2 * 1.0 / 2

print(result)
