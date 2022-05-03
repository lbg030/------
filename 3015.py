# 스택,큐 활용
import sys
HEIGHT, CNT = 0, 1
input = sys.stdin.readline


def solve():
    stk = []
    ans = 0
    for h in arr:
        print(f"{stk}, {h}, ans = {ans}")
        # stack에 현재 사람보다 작은 사람이 있으면, POP하고, answer에 저장된 CNT 추가
        # h값이 입력될 때, top과 h 값만 비교하면 되기 때문에, stack에는 내림차순으로 관리를 할거임.
        while stk and stk[-1][HEIGHT] < h:
            ans += stk.pop()[CNT]
        # 스택이 비어있다면, 입력받은 값과 , cnt(1) 추가
        if not stk:
            stk.append((h, 1))
            continue
        # h와 stack top이 같다면, stk에서 pop 해주고, 같은 키인 사람들 만큼
        if stk[-1][HEIGHT] == h:
            cnt = stk.pop()[CNT]
            ans += cnt
            # 현재 키보다 큰 사람이 있다면, 같은 키가 입력 될 때마다, 그 사람도 볼 수 있음.
            if stk:
                ans += 1
            # 현재 키인 사람과 같은 사람이 입력되면, cnt만큼 있으므로, cnt+1을 해준다.
            stk.append((h, cnt+1))
        # stack이 비어있지 않고, stack top이 더 큰 경우 , 왼쪽 사람만 나는 볼 수 있음.
        else:
            stk.append((h, 1))
            ans += 1
    # print(stk)
    return ans


N = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(N)]
print(solve())
