import sys

a, b, c = map(float, sys.stdin.read().split(" "))

v = [a, b, c]
m = max(v)

s = sum(v)
sl = s - m

if sl <= m:
    area = ((v[0] + v[1]) * v[2]) / 2
    sys.stdout.write(f"Area = {area:.1f}\n")
    exit()

per = s
sys.stdout.write(f"Perimetro = {per:.1f}\n")
