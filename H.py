H, W = map(int, input().split())
g = [input() for _ in range(H)]
vis = [[False] * W for _ in range(H)]

i, j = 0, 0
while True:
    if vis[i][j]:
        print(-1)
        exit(0)
    vis[i][j] = True
    if g[i][j] == 'U' and i != 0:
        i -= 1
    elif g[i][j] == 'D' and i != H - 1:
        i += 1
    elif g[i][j] == 'L' and j != 0:
        j -= 1
    elif g[i][j] == 'R' and j != W - 1:
        j += 1
    else:
        break
print(i + 1, j + 1)
