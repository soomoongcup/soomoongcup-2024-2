n = int(input())
s = input()

count = 0
for i in range(n):
    if not s[i].isalnum():
        count += 1

print(count)