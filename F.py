N = int(input())
s, t = [], []
for i in range(N):
    u, v = input().split()
    s.append(u)
    t.append(v)

for i in range(N):
    can_give_a_nickname = False
    for S in [s[i], t[i]]:
        s_ok = True
        for j in range(N):
            if i != j:
                if S == s[j] or S == t[j]:
                    s_ok = False
        if s_ok:
            can_give_a_nickname = True
    if not can_give_a_nickname:
        print("No")
        exit()

print("Yes")