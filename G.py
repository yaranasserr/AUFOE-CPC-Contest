N, W = map(int, input().split())
A = list(map(int, input().split()))

flag = [0] * (W + 1)

for i in range(N):
    s = A[i]
    if s <= W:
        flag[s] = 1

for i in range(N):
    for j in range(i + 1, N):
        s = A[i] + A[j]
        if s <= W:
            flag[s] = 1

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            s = A[i] + A[j] + A[k]
            if s <= W:
                flag[s] = 1

ans = sum(flag)
print(ans)
