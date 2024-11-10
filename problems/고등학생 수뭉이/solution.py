n = int(input())
s = input()

count = 0
for i in range(len(s)):
    if not ((s[i].isalpha()) or (s[i] == ' ')):
        count += 1

print(count)