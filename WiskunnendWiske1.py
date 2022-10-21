import random

sims = 100_000

#SHORT, BUT INEFFICIENT
def Solve(pos=5, cnt=0):
    if pos == 1: return cnt
    return Solve((lambda x: x - 1 if random.randint(0,9) < 2*(x-1) else 5)(pos), cnt+1)

answ = sum([Solve() for _ in range(sims)])/sims

#LONGER, BUT MORE EFFICIENT
def Solve():
    pos, cnt = 5, 0
    while pos != 1:
        cnt += 1
        pos = pos - 1 if random.randint(0,9) < 2*(pos-1) else 5
    return cnt

answ = sum([Solve() for _ in range(sims)])/sims
