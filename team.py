n = int(input()) # 1 <= n <= 1000

matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

count = 0
for num in matrix:
    if num.count(1) >= 2:
        count += 1

print(count)

