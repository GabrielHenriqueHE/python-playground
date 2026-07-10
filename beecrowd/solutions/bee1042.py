import sys

n = list(map(int, sys.stdin.read().split(" ")))

s = sorted(n)

for i in s:
    sys.stdout.write(f"{str(i)}\n")

sys.stdout.write("\n")

for i in n:
    sys.stdout.write(f"{str(i)}\n")
